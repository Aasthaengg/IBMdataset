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
    n, k = ns()
    a = na()

    dp = [False] * (k + 1)

    for i in range(k + 1):
        for ai in a:
            if i + ai < k + 1:
                dp[i + ai] |= not dp[i]
            else:
                break

    print("First" if dp[k] else "Second")


if __name__ == '__main__':
    main()
