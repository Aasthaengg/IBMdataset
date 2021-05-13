#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

L=list(map(int,input())); n=len(L)
L.reverse();L.append(0)
for i in range(n):

  if L[i] >= 6:
    count += 10-L[i]
    L[i] = 0; L[i+1] += 1

  elif L[i] == 5 and L[i+1] >= 5:
    count += 10-L[i]
    L[i] = 0; L[i+1] += 1

print(count + sum(L))
# print(L)
    

