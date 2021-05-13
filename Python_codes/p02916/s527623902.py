#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count = 0
last = None
for i in range(N):
    count += B[A[i]-1]
    if last and A[i] == last + 1:
        count += C[last-1]
    last = A[i]

print(count)
