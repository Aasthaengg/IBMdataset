#!/usr/bin/env python3
import sys
from bisect import bisect_right

INF = float("inf")


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    dp = [INF]*N
    for i in range(N):
        j = bisect_right(dp, -A[i])
        dp[j] = -A[i]

    print(sum([1 for d in dp if d < INF]))
    # print(dp)


if __name__ == '__main__':
    main()
