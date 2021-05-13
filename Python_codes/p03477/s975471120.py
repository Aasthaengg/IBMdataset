#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, string
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**7)
inf = float('inf')
mod = 10**9+7
ans = 0 ;count = 0 ;pro = 1


a,b,c,d=map(int,input().split())
if a+b-c-d>0:
    print("Left")
if a+b-c-d==0:
    print("Balanced")
if a+b-c-d<0:
    print("Right")

