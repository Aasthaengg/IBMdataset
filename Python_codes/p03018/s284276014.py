#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

s = input()
s = s.replace("BC", "D")
n = len(s)
for i in range (n):
  if s[i] == "A":
    count += 1
  elif s[i] == "D":
    ans += count
  else:
    count = 0
print(ans)

