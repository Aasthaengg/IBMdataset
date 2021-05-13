#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,k=map(int,input().split())
A=list(map(int,input().split()))
mina = min(A)
dp = [0]*(k+1)
for left in range(k+1):
  win = False
  for i, ai in enumerate(A):
    if left - ai >= 0 and dp[left-ai] == 0:
      win = True
    dp[left] = (1 if win else 0)
print("First"if dp[k] else "Second")

    
