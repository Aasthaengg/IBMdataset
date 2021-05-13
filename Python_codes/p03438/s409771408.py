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
    b = na()

    a_cnt = 0
    b_cnt = 0

    for ai, bi in zip(a, b):
        tmp = bi - ai
        if tmp < 0:
            b_cnt += abs(tmp)
        elif tmp > 0:
            a_cnt += (tmp + 1) // 2
            b_cnt += tmp % 2
        # print(ai, bi, a_cnt, b_cnt)

    print("Yes" if a_cnt >= b_cnt else "No")


if __name__ == '__main__':
    main()
