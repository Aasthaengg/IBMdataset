#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

seen = {}


def luka(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    if n in seen.keys():
        return seen[n]
    else:
        seen[n] = luka(n-1) + luka(n-2)
        return seen[n]


N = int(input())
print(luka(N))

