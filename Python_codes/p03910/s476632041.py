#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
now = n
for i in range(1,n+1):
  if now == i:
    key = -1
    top = i
    break
  elif now - i < 0:
    key = i - now
    top = i
    break
  else:
    now -= i
for i in range(1,top+1):
  if i != key:print(i)