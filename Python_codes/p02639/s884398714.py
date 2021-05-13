#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

X = list(map(int, input().split()))

for i in range(5):
    if X[i] == 0:
        print(i+1)

