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
    Hs = list(map(int, input().split()))

    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if Hs[i] >= Hs[i+1]:
            cnt += 1
            max_cnt = max([max_cnt, cnt])
        else:
            cnt = 0
    print(max_cnt)


if __name__ == '__main__':
    main()
