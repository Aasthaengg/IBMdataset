import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8[:](i8,i8,i8,i8[:,:],i8[:,:])", cache=True)
def solve(N, M, Q, LR, pq):
    S = np.zeros(shape=(N + 1, N + 1), dtype=np.int64)
    for i in range(M):
        L, R = LR[i]
        S[L][R] += 1
    for i in range(N + 1):
        S[i] = np.cumsum(S[i])

    ans = np.zeros(shape=Q, dtype=np.int64)
    for i in range(Q):
        p, q = pq[i]
        for j in range(p, q + 1):
            ans[i] += S[j][q] - S[j][p - 1]

    return ans


def main():
    N, M, Q = map(int, input().split())
    LR = np.zeros(shape=(M, 2), dtype=np.int64)
    for i in range(M):
        LR[i] = input().split()
    pq = np.zeros(shape=(Q, 2), dtype=np.int64)
    for i in range(Q):
        pq[i] = input().split()

    ans = solve(N, M, Q, LR, pq)

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
