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
def slv(N, K, AB):
    g = defaultdict(list)
    for a, b in AB:
        g[a].append(b)
        g[b].append(a)

    s = [(1, -1, 0, 0)]
    ans = [1] * (N+1)
    while s:
        u, p, k1, k2 = s.pop()
        ans[u] = K - k1 - k2

        cu = 0
        for v in g[u]:
            if v == p:
                continue
            s.append((v, u, 1, cu+k1))
            cu += 1

    M = 10**9+7
    return reduce(lambda x, y: (x * y) % M, ans)



def main():
    N, K = read_int_n()
    AB = [read_int_n() for _ in range(N-1)]
    print(slv(N, K, AB))


if __name__ == '__main__':
    main()
