#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
INF = 10**19
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
    W, H, x, y = map(int, input().split())

    if x == W / 2 and y == H / 2:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)


if __name__ == '__main__':
    main()
