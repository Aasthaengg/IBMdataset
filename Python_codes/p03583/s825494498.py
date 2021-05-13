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
    N = ni()
    lim = 3500

    for h in range(1, lim + 1):
        for n in range(1, lim + 1):
            up = N * h * n
            down = 4 * h * n - N * n - N * h
            if down != 0:
                if up % down == 0:
                    if 0 < up // down:
                        print(h, n, up // down)
                        exit(0)


if __name__ == '__main__':
    main()
