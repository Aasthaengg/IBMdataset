import sys

import numba as nb
import numpy as np

input = sys.stdin.readline
INF = float("inf")


@nb.njit("i8(i8,i8,i8[:])")
def solve(N, K, h):
    dp = np.zeros(N, dtype=np.int64)
    for i in range(1, N):
        k = min(K, i)
        dp[i] = np.min(dp[i - k:i] + np.abs(h[i] - h[i - k:i]))
    return dp[-1]


def main():
    N, K = map(int, input().split())
    h = np.array(input().split(), dtype=np.int64)

    ans = solve(N, K, h)
    print(ans)


if __name__ == "__main__":
    main()
