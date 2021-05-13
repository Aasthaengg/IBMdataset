# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, K, A):
    c = Counter()
    for a in A:
        for i in range(64):
            if a & (1 << i) != 0:
                c[i] += 1

    x = 0
    for i in range(63, -1, -1):
        m = 1 << i
        if x + m > K:
            continue
        if c[i] <= N // 2:
            x += m

    return sum(map(lambda a: x ^ a, A))


def main():
    N, K = read_int_n()
    A = read_int_n()

    print(slv(N, K, A))


if __name__ == '__main__':
    main()
