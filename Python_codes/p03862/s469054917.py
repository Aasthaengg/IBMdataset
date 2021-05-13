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
import heapq
import decimal
# import statistics
import queue
import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, x = ns()
    a = na()

    ans = 0

    for i in range(1, n):
        tmp = a[i - 1] + a[i]
        if tmp > x:
            a[i] = max(0, a[i] - (tmp - x))
            ans += tmp - x

    print(ans)


if __name__ == '__main__':
    main()
