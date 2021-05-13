# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul

sys.setrecursionlimit(10000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


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


move = None
tx = None
ty = None


@mt
def slv(N, A):
    mx = max(A)
    mn = min(A)
    ans = []
    if abs(mx) > abs(mn):
        idx = A.index(mx)
        for i in range(N):
            if A[i] < 0:
                ans.append((idx, i))
                A[i] += mx
        for i in range(1, N):
            ans.append((i-1, i))
            A[i] += A[i-1]
    else:
        idx = A.index(mn)
        for i in range(N):
            if A[i] > 0:
                ans.append((idx, i))
                A[i] += mn
        for i in range(N-1, 0, -1):
            ans.append((i, i-1))
            A[i-1] += A[i]

    print(len(ans))
    for x, y in ans:
        print(x+1, y+1)


def main():
    N = read_int()
    A = read_int_n()
    slv(N, A)


if __name__ == '__main__':
    main()
