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
    n = ni()
    a = na()

    min_n = min(a)
    max_n = max(a)
    minflg = True
    maxflg = True

    d = []
    for ai in a:
        if ai == min_n and minflg:
            minflg = False
            continue
        if ai == max_n and maxflg:
            maxflg = False
            continue
        d.append(ai)

    ans = []
    for ai in d:
        if ai < 0:
            ans.append([max_n, ai])
            max_n -= ai
        else:
            ans.append(([min_n, ai]))
            min_n -= ai
    ans.append([max_n, min_n])

    print(max_n - min_n)

    for a, b in ans:
        print(a, b)


if __name__ == '__main__':
    main()
