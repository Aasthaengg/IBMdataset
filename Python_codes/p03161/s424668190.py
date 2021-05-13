import sys

import numba as nb
import numpy as np

input = sys.stdin.readline
INF = float("inf")


@nb.njit("i8(i8,i8,i8[:])")
def solve(N, K, h):
    dp = np.zeros(N, dtype=np.int64)
    for i in range(1, N):
        min_cost = INF
        for k in range(1, min(K + 1, i + 1)):
            cost = dp[i - k] + abs(h[i] - h[i - k])
            if cost < min_cost:
                min_cost = cost
        dp[i] = min_cost
    return dp[-1]


def main():
    N, K = map(int, input().split())
    h = np.array(input().split(), dtype=np.int64)

    ans = solve(N, K, h)
    print(ans)


if __name__ == "__main__":
    main()
