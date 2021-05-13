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
        i_s = binary_search(S, x)
        i_t = binary_search(T, x)
        for s in (S[i_s - 1], S[i_s]):
            for t in (T[i_t - 1], T[i_t]):
                dist_s2t = abs(x - s) + abs(s - t)
                dist_t2s = abs(x - t) + abs(t - s)
                min_dist = min(min_dist, dist_s2t, dist_t2s)
        ans[q] = min_dist
    return ans


def main():
    A, B, Q = map(int, input().split())
    S = np.zeros(shape=(A + 2), dtype=np.int64)
    T = np.zeros(shape=(B + 2), dtype=np.int64)
    X = np.zeros(shape=Q, dtype=np.int64)
    for i in range(1, A + 1):
        S[i] = int(input())
    for i in range(1, B + 1):
        T[i] = int(input())
    for i in range(Q):
        X[i] = int(input())

    S[0] = T[0] = -10 ** 11
    S[-1] = T[-1] = 10 ** 11

    ans = solve(Q, S, T, X)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
