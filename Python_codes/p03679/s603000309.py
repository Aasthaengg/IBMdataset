#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, string
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf')
mod = 10**9+7
ans = 0 ;count = 0 ;pro = 1

x,a,b=map(int,input().split())
ab=b-a
if ab<=0:
    print("delicious")
elif 0<ab<=x:
    print("safe")
else:
    print("dangerous")