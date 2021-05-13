#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,k=map(int,input().split())
A=list(map(int,input().split()))
dp = [False]*(k+1)
for left in range(k+1):
  for i, ai in enumerate(A):
    if left - ai >= 0:dp[left] |= not dp[left-ai]
print("First"if dp[k] else "Second")

    
