#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if ans < a:
        ans = a; mans = b
print(ans+mans)