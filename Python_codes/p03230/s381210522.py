# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 2**62-1

def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N):
    for k in range(1000):
        if (k*k-k) % 2 == 0 and (k*k-k) // 2 == N:
            break
    else:
        print('No')
        return

    c = 1
    S = [set() for _ in range(k)]
    for i in range(k):
        for j in range(i+1, k):
            S[i].add(c)
            S[j].add(c)
            c += 1
    print('Yes')
    print(k)
    for s in S:
        print(len(s), ' '.join(map(str, s)))



def main():
    N = read_int()
    (slv(N))


if __name__ == '__main__':
    main()
