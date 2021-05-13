#!/usr/bin/env python3

import math
import sys
from collections import defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect
from heapq import heappop, heappush
from fractions import gcd
import copy


def next_line():
    return input()


def next_int():
    return int(input())


def int_ar():
    return list(map(int, input().split()))


def int_ar_mul(size):
    return [int(input()) for _ in range(size)]


def str_ar(size):
    return [input() for _ in range(size)]


def ints():
    return map(int, input().split())


def strs():
    return input().split()


def main():
    alp = "zabcdefghijklmnopqrstuvwxy"
    n = next_int()
    str = ""
    while n > 0:
        str = alp[n % 26] + str
        if n % 26 == 0:
            n -= 26
        n //= 26
    print(str)


if __name__ == '__main__':
    main()
