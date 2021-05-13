import sys

# import re
import math
import collections
# import decimal
# import bisect
# import itertools
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
    s = ni()

    deka = 10 ** 9
    x1 = s // deka
    tmp = s % deka

    if tmp:
        y1 = deka - tmp
    else:
        x1 -= 1
        y1 = 0

    print(x1 + 1, y1, 1, deka, 0, 0)


if __name__ == '__main__':
    main()
