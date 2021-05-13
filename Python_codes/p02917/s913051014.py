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
    Bs = list(map(int, input().split()))

    Asum = 0
    for i in range(N):
        if i == 0:
            Asum += Bs[0]
        elif i == N - 1:
            Asum += Bs[N-2]
        else:
            Asum += min([Bs[i-1], Bs[i]])
    print(Asum)


if __name__ == '__main__':
    main()
