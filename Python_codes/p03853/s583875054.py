#!/usr/bin/env python
import sys
from collections import Counter
from itertools import permutations, combinations
from fractions import gcd
#from math import gcd
from math import ceil, floor
import bisect
sys.setrecursionlimit(10 ** 6)
inf = float("inf")

def input():
    return sys.stdin.readline()[:-1]

def main():
    h, w = map(int, input().split())
    C = [None] * h
    for i in range(h):
        C[i] = input()
    for i in range(h):
        print(C[i])
        print(C[i])

if __name__ == '__main__':
    main()
