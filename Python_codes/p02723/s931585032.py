#!/usr/bin/env python
import sys
from collections import Counter
from itertools import permutations, combinations
from fractions import gcd
from math import ceil, floor
import bisect
sys.setrecursionlimit(10 ** 6)
inf = float("inf")

def input():
    return sys.stdin.readline()[:-1]

def main():
    s = input()
    if s[2] == s[3] and s[4] == s[5]:
        print("Yes")
    else:
        print("No") 

if __name__ == '__main__':
    main()

