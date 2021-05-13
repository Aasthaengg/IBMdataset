#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

s=set()
data=[1,7,9,4]
for si in map(int,input().split()):
    if si in data:
        s.add(si)
print("YES" if len(s)==4 else "NO")