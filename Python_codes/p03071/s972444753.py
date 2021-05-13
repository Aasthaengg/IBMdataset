#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())

count = 0
for i in range(2):
    if A > B:
        count += A
        A -= 1
    else:
        count += B
        B -= 1

print(count)
