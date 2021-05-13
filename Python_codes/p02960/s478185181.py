import sys

# import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

# from numba import jit
# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    d = len(s)

    dp = [[0] * 13 for _ in range(d)]

    x = s[0]
    if x == "?":
        for i in range(10):
            nummod = (i * pow(10, d - 1, 13)) % 13
            dp[0][nummod] = 1
    else:
        nummod = (int(x) * pow(10, d - 1, 13)) % 13
        dp[0][nummod] = 1

    for i in range(1, d):
        x = s[i]
        if x == "?":
            for j in range(10):
                nummod = (j * pow(10, d - i - 1, 13)) % 13
                for k in range(13):
                    count = dp[i - 1][k]
                    nextmod = (k + nummod) % 13
                    dp[i][nextmod] += count
                    dp[i][nextmod] = dp[i][nextmod] % MOD
        else:
            nummod = (int(x) * pow(10, d - i - 1, 13)) % 13
            for j in range(13):
                count = dp[i - 1][j]
                nextmod = (j + nummod) % 13
                dp[i][nextmod] += count
                dp[i][nextmod] = dp[i][nextmod] % MOD

    print(dp[-1][5])


if __name__ == '__main__':
    main()
