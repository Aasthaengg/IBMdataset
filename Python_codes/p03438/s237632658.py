#!/usr/bin/env python3
# input
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for i in range(n):
    if a[i] > b[i]:
        res -= a[i] - b[i]
    else:
        res += (b[i] - a[i]) // 2
if res >= 0:
    print("Yes")
else:
    print("No")
