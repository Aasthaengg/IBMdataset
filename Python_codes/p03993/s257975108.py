#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
A = list(map(int,input().split()))
for i in range(n): A[i] -= 1
for i in range(n):
  if not A[i] > i:continue
  else:
    if A[A[i]] == i:ans += 1
print(ans)