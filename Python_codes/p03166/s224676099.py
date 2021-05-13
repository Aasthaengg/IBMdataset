#!/usr/bin/env python
import sys
import re
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def get_longest(x, longest, edges):
    if longest[x] is not None:
        return longest[x]
    if not edges[x]:
        longest[x] = 0
    else:
        result = max([get_longest(y, longest, edges)
                      for y in edges[x]])
        longest[x] = result + 1
    return longest[x]


def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())
    #ps = list(map(int, input().split()))

    N, M = map(int, input().split())

    edges = defaultdict(set)
    for i in range(M):
        x, y = map(int, input().split())
        edges[x].add(y)

    longest = [None] * (N + 1)
    for x in range(N):
        x += 1
        if longest[x] is None:
            get_longest(x, longest, edges)

    print(max(longest[1:]))


if __name__ == '__main__':
    main()
