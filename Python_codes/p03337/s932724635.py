#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = count = 0

a,b=map(int,input().split())
print(max(a+b,a-b,a*b))