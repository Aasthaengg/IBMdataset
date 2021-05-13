#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a,b,k=map(int,input().split())
for i in range(k):
    if i%2==0:
        a//=2
        b+=a
    else:
        b//=2
        a+=b
print(a,b)
