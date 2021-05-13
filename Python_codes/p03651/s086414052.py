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
    # 最大公約数
    import fractions
    from functools import reduce

    n, k = ns()
    a = na()

    gcdans = reduce(fractions.gcd, a)

    maximum = max(a)
    if maximum - k >= 0 and (maximum - k) % gcdans == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
