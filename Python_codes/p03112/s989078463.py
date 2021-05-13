import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8(i8[:],i8)", cache=True)
def binary_search(a, key):
    """Meguru type binary search"""
    ng = -1
    ok = len(a)

    def is_ok(a, key, idx):
        if key <= a[idx]:
            return True
        else:
            return False

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(a, key, mid):
            ok = mid
        else:
            ng = mid

    return ok


@nb.njit("i8[:](i8,i8[:],i8[:],i8[:])", cache=True)
def solve(Q, S, T, X):
    ans = np.zeros(shape=Q, dtype=np.int64)
    INF = 10 ** 11
    for q, x in enumerate(X):
        min_dist = INF
        # x --> s --> t
        i = binary_search(S, x)
        if 0 < i:
            l_s = S[i - 1]
            dist_s = abs(x - l_s)
            j = binary_search(T, l_s)
            l_t, r_t = T[j - 1], T[j]
            dist_t = min(abs(l_s - l_t), abs(r_t - l_s)) if 0 < j else abs(r_t - l_s)
            min_dist = min(min_dist, dist_s + dist_t)
        r_s = S[i]
        dist_s = abs(r_s - x)
        j = binary_search(T, r_s)
        l_t, r_t = T[j - 1], T[j]
        dist_t = min(abs(r_s - l_t), abs(r_t - r_s)) if 0 < j else abs(r_t - r_s)
        min_dist = min(min_dist, dist_s + dist_t)

        # x --> t --> s
        i = binary_search(T, x)
        if 0 < i:
            l_t = T[i - 1]
            dist_t = abs(l_t - x)
            j = binary_search(S, l_t)
            l_s, r_s = S[j - 1], S[j]
            dist_s = min(abs(l_t - l_s), abs(r_s - l_t)) if 0 < j else abs(r_s - l_t)
            min_dist = min(min_dist, dist_s + dist_t)
        r_t = T[i]
        dist_t = abs(r_t - x)
        j = binary_search(S, r_t)
        l_s, r_s = S[j - 1], S[j]
        dist_s = min(abs(r_t - l_s), abs(r_s - r_t)) if 0 < j else abs(r_s - r_t)
        min_dist = min(min_dist, dist_s + dist_t)

        ans[q] = min_dist
    return ans


def main():
    A, B, Q = map(int, input().split())
    S = np.zeros(shape=A, dtype=np.int64)
    T = np.zeros(shape=B, dtype=np.int64)
    X = np.zeros(shape=Q, dtype=np.int64)
    for i in range(A):
        S[i] = int(input())
    for i in range(B):
        T[i] = int(input())
    for i in range(Q):
        X[i] = int(input())

    ans = solve(Q, S, T, X)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
