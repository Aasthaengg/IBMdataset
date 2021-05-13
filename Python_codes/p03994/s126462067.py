#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

goal = ord("z") + 1 
s = input()
k = int(input())
n = len(s)
ans = [0] * n
for i,si in enumerate(s):
  if si == "a":ans[i] = "a"
  elif goal - ord(si) <= k:
    k -= goal - ord(si)
    ans[i] = "a"
  else:
    ans[i] = si
m = k % 26
ans[-1] = chr((ord(ans[-1]) - ord("a") + m)%26 + ord("a"))
print(*ans,sep="")