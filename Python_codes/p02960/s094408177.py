import sys

import numba as nb
import numpy as np

input = sys.stdin.readline

P = 10 ** 9 + 7
Q = 13


@nb.njit("i8(i8[:])", cache=True)
def solve(S):
    N = len(S)
    dp = np.zeros(shape=(N + 1, Q), dtype=np.int64)
    dp[0][0] = 1
    for i in range(N):
        D = S[i]
        if D == -1:
            for d in range(10):
                for j in range(Q):
                    dp[i + 1][(10 * j + d) % Q] += dp[i][j]
        else:
            for j in range(Q):
                dp[i + 1][(10 * j + D) % Q] += dp[i][j]

        for j in range(Q):
            dp[i + 1][j] %= P

    return dp[N][5]


def main():
    S = input().rstrip()

    S = np.array([int(s) if s != "?" else -1 for s in S], dtype=np.int64)
    ans = solve(S)
    print(ans)


if __name__ == "__main__":
    main()
