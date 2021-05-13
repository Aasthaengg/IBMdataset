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


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        error_print(e - s, 'sec')
        return ret

    return wrap


def ref(L):
    L = int(L, base=2)
    ans = 0
    for a in range(L+1):
        for b in range(L+1):
            if (a + b <= L) and (a ^ b == a + b):
                # print(a, b, a^ b, a+b)
                ans += 1
    return ans



@mt
def slv(L):
    M = 10**9 + 7
    ans = 1
    m = 0
    for b in map(int, L):
        m *= 3
        if b == 1:
            m += ans
            ans *= 2

        ans %= M
        m %= M
    ans += m
    ans %= M
    return ans


def main():
    L = read_str()
    print(slv(L))


if __name__ == '__main__':
    main()
