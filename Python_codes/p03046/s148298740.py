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
def slv(M, K):
    if M == 0:
        if K == 0:
            print(0, 0)
        else:
            print(-1)
    elif M == 1:
        if K == 0:
            print(0, 0, 1, 1)
        else:
            print(-1)
    else:
        if K < 2**M:

            for i in range(2**M):
                if i == K:
                    continue
                print(i, '', end='')
            print(K, '', end='')

            for i in range(2**M-1, -1, -1):
                if i == K:
                    continue
                print(i, '', end='')
            print(K, '', end='')

        else:
            print(-1)


def main():
    M, K = read_int_n()
    (slv(M, K))


if __name__ == '__main__':
    main()
