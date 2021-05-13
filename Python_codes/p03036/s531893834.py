#!/usr/bin/env python
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor

def main():
    #N, M = map(int, input().split())
    r, D, x = map(int, input().split())

    for i in range(10):
        x = r * x - D
        print(x)


if __name__ == '__main__':
    main()
