#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,a,b = map(int,input().split())
X = list(map(int,input().split()))
dis = [0]*(n-1)
for i in range(1,n):
  dis[i-1]= X[i]-X[i-1]
for di in dis:
  if di*a <= b:
    ans += di*a
  else:
    ans += b
print(ans)