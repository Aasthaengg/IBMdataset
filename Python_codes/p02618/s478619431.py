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
    return D, C, S


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
def change_schedule(D, C, S, T, d, q, cumsat):
    """d日目のコンテストをqに変更する
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


@njit
def greedy(D, C, S):
    T = np.zeros(D, dtype=np.int32)
    last = np.zeros(26, dtype=np.int32)
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


@njit
def solve(D, C, S):
    cumsat, T = greedy(D, C, S)
    for t in T:
        print(t+1)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
