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
    naf = lambda: list(map(float, sys.stdin.readline().split()))

    n = ni()
    p = naf()

    dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    dp[0][0] = 1

    # dp[i][j] : pのうちi個めまでを投げて、表がj個出る確率
    for i in range(n):
        for j in range(i+1):
            dp[i + 1][j + 1] += dp[i][j] * p[i]
            dp[i + 1][j] += dp[i][j] * (1 - p[i])

    print(sum(dp[n][(n + 1) // 2:]))


if __name__ == '__main__':
    main()
