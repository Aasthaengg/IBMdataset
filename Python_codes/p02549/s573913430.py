#!/usr/bin/env python3
import sys
import numpy as np

# import numba
# from numba import njit, b1, i4, i8, f8

input = sys.stdin.readline
mod = 998244353


def I():
    return int(input())


def MI():
    return map(int, input().split())


# @njit((i8, i8[:]), cache=True)
def main(N, steps):
    dp = np.zeros(N + 1, np.int64)
    dpsum = np.zeros(N + 1, np.int64)
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2, N + 1):
        for l, r in steps:
            li = i - r
            ri = i - l
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
            dp[i] %= mod
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= mod

    return dp[N]


N, K = MI()

steps = []
for _ in range(K):
    l, r = MI()
    steps.append((l, r))


print(main(N, steps))
