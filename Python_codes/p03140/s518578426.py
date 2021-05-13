#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
a=input()
b=input()
c=input()
def f(a,b,c):
  re=2
  if a==b:
    re-=1
  if c==b:
    re-=1
  if a==c:
    re-=1
  return max(0,re)
for i in range(n):
  count += f(a[i],b[i],c[i])
print(count)