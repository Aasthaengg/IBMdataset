#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, string
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**7)
inf = float('inf')
mod = 10**9+7
ans = inf ;count = 0 ;pro = 1
a,b,c=map(int,input().split())
if a+b>=c:
    print("Yes")
else:
    print("No")