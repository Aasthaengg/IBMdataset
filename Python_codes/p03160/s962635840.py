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
    a = na()

    dp = [INF for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        nxt1 = min(i + 1, n - 1)
        cost = abs(a[i] - a[nxt1])
        dp[nxt1] = min(dp[nxt1], dp[i] + cost)

        nxt2 = min(i + 2, n - 1)
        cost = abs(a[i] - a[nxt2])
        dp[nxt2] = min(dp[nxt2], dp[i] + cost)

    print(dp[n - 1])


if __name__ == '__main__':
    main()
