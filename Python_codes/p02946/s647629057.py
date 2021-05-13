#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

K, X = map(int, input().split())

A = []
for i in range(X-K+1, X+K):
    A.append(str(i))

res = " ".join(A)
print(res)

