# strat_localsearch_fine
import sys
input = sys.stdin.readline
import numpy as np
from numba import njit


def read():
    D = int(input().strip())
    C = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
    S = np.empty((D, 26), dtype=np.int32)
    for i in range(D):
        s = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
        S[i, :] = s[:]
    M = 100000
    RD = np.random.randint(D, size=(M, ), dtype=np.int32)
    RQ = np.random.randint(26, size=(M, ), dtype=np.int32)
    DQ = np.stack([RD, RQ]).T
    COND = np.random.randint(2, size=(M, ), dtype=np.bool)
    return D, C, S, M, DQ, COND


@njit
def diff_satisfaction(C, S, d, p, last):
    """d日目にコンテストpを開催するときの、満足度の更新量を求める
    """
    v = 0
    for i in range(26):
        v -= C[i] * (d - last[i])
    v += C[p] * (d - last[p])
    v += S[d, p]
    return v



@njit
def evaluate(D, C, S, d, p, last, k=13):
    """d日目にコンテストpを開催し、その後d+k日目までコンテストが開催されないときの、満足度の更新差分を求める
    """
    v = diff_satisfaction(C, S, d, p, last)
    for e in range(d+1, min(d+k, D)):
        for i in range(26):
            v -= C[i] * (e - last[i])
        v += C[p] * (d - last[p])
    return v


@njit
def greedy_fine(D, C, S):
    T = np.zeros(D, dtype=np.int32)
    last = -np.ones(26, dtype=np.int32)
    cumsat = 0
    for d in range(D):
        
        max_p = 0
        max_e = -999999999

        # select contest greedily
        for p in range(26):
            e = evaluate(D, C, S, d, p, last, k=8)
            
            if e > max_e:
                max_p = p
                max_e = e
        
        # update schedule
        cumsat += diff_satisfaction(C, S, d, max_p, last)
        T[d] = max_p
        last[max_p] = d
    return cumsat, T


@njit
def update(D, C, S, T, d, q, cumsat):
    """1点更新: d日目のコンテストをqに変更する
    """
    p = T[d]
    dp1, dq1 = -1, -1
    dp3, dq3 = D, D
    for i in range(0, d):
        if T[i] == p: 
            dp1 = i
        if T[i] == q:
            dq1 = i
    for i in range(D-1, d, -1):
        if T[i] == p:
            dp3 = i
        if T[i] == q:
            dq3 = i
    cumsat = cumsat - S[d, p] + S[d, q] - C[p] * (dp3-d) * (d-dp1) + C[q] * (dq3-d) * (d-dq1)
    return cumsat



def swap(D, C, S, T, d0, p0, d1, p1, cumsat):
    """2点スワップ: d0日目のコンテストp0とd1日目のコンテストp1を交換する
    """
    cumsat = update(D, C, S, T, d0, p1, cumsat)
    cumsat = update(D, C, S, T, d1, p0, cumsat)
    return cumsat


@njit
def greedy(D, C, S):
    T = np.zeros(D, dtype=np.int32)
    last = -np.ones(26, dtype=np.int32)
    cumsat = 0
    for d in range(D):
        max_p = 0
        max_diff = -999999999

        # select contest greedily
        for p in range(26):
            diff = diff_satisfaction(C, S, d, p, last)
            if diff > max_diff:
                max_p = p
                max_diff = diff
        
        # update schedule
        cumsat += max_diff
        T[d] = max_p
        last[max_p] = d
    return cumsat, T



def solve(D, C, S, M, DQ, COND):
    cumsat, T = greedy(D, C, S)
    for i in range(M):
        d, q = DQ[i, :]
        if COND[i]:
            newsat = update(D, C, S, T, d, q, cumsat)
            if newsat > cumsat:
                cumsat = newsat
                T[d] = q
        else:
            d0, d1 = d, min(d+1+q//2, D-1)
            newsat = swap(D, C, S, T, d0, T[d0], d1, T[d1], cumsat)
            if newsat > cumsat:
                cumsat = newsat
                T[d1], T[d0] = T[d0], T[d1]
    for t in T:
        print(t+1)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
