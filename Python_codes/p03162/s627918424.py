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

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    n = ni()
    a = [na() for _ in range(n)]

    dp = [[0 for _ in range(3)] for __ in range(n + 1)]
    dp[0] = 0, 0, 0

    for i in range(n):
        for j in range(3):
            for k in range(1, 3):
                idx = (j + k) % 3
                dp[i + 1][idx] = max(dp[i + 1][idx], dp[i][j] + a[i][idx])

    print(max(dp[n]))

if __name__ == '__main__':
    main()
