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

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    a = na()

    a.sort()

    idx = 0

    tmp_size = a[0]
    for i in range(1, n):
        if tmp_size >= (a[i] + 1) // 2:
            tmp_size += a[i]
            continue
        else:
            tmp_size += a[i]
            idx = i

    print(n - idx)


if __name__ == '__main__':
    main()
