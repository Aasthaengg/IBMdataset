#!/usr/bin/env python
import sys
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def main():
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())

    #N, Q = map(int, input().split())

    N = int(input())

    print(N*(N-1)//2)


if __name__ == '__main__':
    main()
