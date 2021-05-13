#!/usr/bin/env python
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor

def main():
    #N, M = map(int, input().split())
    A, B = map(int, input().split())

    if A <= 5:
        print(0)
    elif A <= 12:
        print(B // 2)
    else:
        print(B)

if __name__ == '__main__':
    main()
