#!/usr/bin/env python
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor


def main():
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())

    N = int(input())
    As = list(map(int, input().split()))

    allprod = 1
    for A in As:
        allprod *= A

    total = 0
    for A in As:
        total += allprod / A

    print(allprod / total)


if __name__ == '__main__':
    main()