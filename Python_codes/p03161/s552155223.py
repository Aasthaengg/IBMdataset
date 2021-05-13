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
    n, k = ns()
    a = na()

    dp = [INF for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        for j in range(k):
            if i + j + 1 < n:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i] + abs(a[i] - a[i + j + 1]))
            else:
                break

    print(dp[n - 1])


if __name__ == '__main__':
    main()
