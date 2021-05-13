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
    
    S = input().strip()
    T = input().strip()

    cnt = 0
    for s, t in zip(S, T):
        if s == t:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
