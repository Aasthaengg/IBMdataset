import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
nb = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    s = list(input())
    l = len(s)
    dp = [[0 for _ in range(13)] for __ in range(l + 1)]
    dp[0][0] = 1

    for i, si in enumerate(s):
        base = pow(10, l - i - 1, 13)

        if si == "?":
            for k in range(10):
                tmp = base * k % 13
                for j in range(13):
                    dp[i + 1][(j + tmp) % 13] += dp[i][j]
                    dp[i + 1][(j + tmp) % 13] %= MOD
        else:
            si = int(si)
            tmp = base * si % 13
            for j in range(13):
                dp[i + 1][(j + tmp) % 13] += dp[i][j]
                dp[i + 1][(j + tmp) % 13] %= MOD

    print(dp[l][5])


if __name__ == '__main__':
    main()
