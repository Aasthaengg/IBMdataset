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

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(gcd(*A))

if __name__ == '__main__':
    main()
