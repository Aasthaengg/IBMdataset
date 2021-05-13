#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b

def main():
    N, K = map(int, input().split())

    p = 0
    for i in range(1, N + 1):
        a = K / i
        b = 1
        while b < a:
            b *= 2
        p += (1 / N) * (1 / b)
    print(p)


if __name__ == '__main__':
    main()
