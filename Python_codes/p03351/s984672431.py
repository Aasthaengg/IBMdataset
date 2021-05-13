#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = count = 0

a,b,c,d=map(int,input().split())
if abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d):
    print("Yes")
else:
    print("No")