#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


N = int(input())
S, T = input().split()

res = ""
for i in range(N):
    res += S[i] + T[i]

print(res)