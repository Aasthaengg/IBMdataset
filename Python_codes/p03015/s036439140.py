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
    dp1 = [0 for _ in range(l + 1)]
    dp2 = [0 for _ in range(l + 1)]
    dp1[0] = 1

    for i in range(l):
        if s[i] == "1":
            dp1[i + 1] = dp1[i] * 2
            dp2[i + 1] = dp1[i] + dp2[i] * 3
        else:
            dp1[i + 1] = dp1[i]
            dp2[i + 1] = dp2[i] * 3
        dp1[i + 1] %= MOD
        dp2[i + 1] %= MOD

    print((dp1[l] + dp2[l]) % MOD)


if __name__ == '__main__':
    main()
