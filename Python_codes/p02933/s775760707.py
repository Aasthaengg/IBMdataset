#!/usr/bin/env python
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor


def main():
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())

    a = int(input())
    s = input()

    if a >= 3200:
        print(s)
    else:
        print("red")


if __name__ == '__main__':
    main()
