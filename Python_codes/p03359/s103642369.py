#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = 1
count = 0

a,b=map(int,input().split())
if a>b:
    print(a-1)
else:
    print(a)