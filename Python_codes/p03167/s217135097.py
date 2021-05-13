#!/usr/bin/env python
import sys
import re
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())
    #ps = list(map(int, input().split()))

    H, W = map(int, input().split())
   
    dp = [[0]*W for i in range(H)]
    route = []
    for h in range(H):
        As = input().strip()
        route.append(As)

    for h in range(H):
        for w in range(W):
            if h == 0 and w == 0:
                dp[h][w] = 1
                continue
            if h > 0 and route[h-1][w] != '#':
                dp[h][w] += dp[h-1][w]
            if w > 0 and route[h][w-1] != '#':
                dp[h][w] += dp[h][w-1]

    print(dp[H-1][W-1] % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
