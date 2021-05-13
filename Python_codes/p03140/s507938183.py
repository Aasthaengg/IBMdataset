#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
a,b,c=[input() for i in range(3)]
for i in range(n):
  ans += len(set((a[i],b[i],c[i]))) - 1
print(ans)