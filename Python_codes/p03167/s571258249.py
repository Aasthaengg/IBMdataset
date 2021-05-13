import sys
# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    h, w = ns()
    mat = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for __ in range(h)]
    dp[0][0] = 1

    def calc(x, y, val):
        if x >= w or y >= h:
            return
        if mat[y][x] == "#":
            return
        dp[y][x] += val
        dp[y][x] %= MOD
        return

    for y in range(h):
        for x in range(w):
            calc(x + 1, y, dp[y][x])
            calc(x, y + 1, dp[y][x])
    print(dp[h - 1][w - 1])


if __name__ == '__main__':
    main()
