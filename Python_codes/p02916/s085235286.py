#!/usr/bin/env python
import sys
import re
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())
    #ps = list(map(int, input().split()))

    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))

    sat = 0
    prev = None
    for i in range(N):
        A = As[i]
        sat += Bs[A-1]
        if prev is not None and prev + 1 == A:
            sat += Cs[prev - 1]
        prev = A

    print(sat)





if __name__ == '__main__':
    main()
