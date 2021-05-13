#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
AB = [tuple(map(int,input().split())) for i in range(n)]
AB.sort(key = lambda tup:tup[0]+tup[1],reverse  = True)
for i in range(n):
  if i % 2 == 0:
    ans += AB[i][0]
  else:
    ans -= AB[i][1]
print(ans)
# print(AB)