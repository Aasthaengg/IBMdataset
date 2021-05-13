#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


A, B, T = map(int, input().split())

i = 1
count = 0
while i*A < T + 0.5:
    count += B
    i += 1

print(count)
