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
    def combinations_count(n, r):
        if n > 1:
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
        else:
            return 0

    n = ni()
    a = na()

    a.sort()

    max_ai = max(a)
    idx = bisect.bisect_left(a, max_ai // 2)

    r = -1

    r = a[max(0, idx - 1)]
    if a[idx] != max_ai:
        r = a[idx] if abs(a[idx] - max_ai / 2) < abs(r - max_ai / 2) else r

    print(max_ai, r)


if __name__ == '__main__':
    main()
