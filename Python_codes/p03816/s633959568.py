#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
A = list(map(int,input().split()))
data = [0] * (10**5+1)
for ai in A:
  data[ai] += 1
for i ,di in enumerate(data):
  if di >= 3 and di%2 == 1:
    data[i] =1
  elif di >= 3:
    data[i] = 2
c1 = c2 = 0
for i,di in enumerate(data):
  if di == 1:
    c1 += 1
  elif di == 2:
    c2 += 1

print(c1+c2//2*2)