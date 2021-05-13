#!/usr/bin/env python3
import sys
from bisect import bisect_left
from bisect import bisect_right

INF = float("inf")


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    dp = [INF]*N
    for i in range(N):
        j = bisect_right(dp, -A[i])
        dp[j] = -A[i]

    print(bisect_left(dp, INF))


if __name__ == '__main__':
    main()