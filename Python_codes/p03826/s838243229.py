#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf')
ans = 0 ;count = 0 ;pro = 1

a,b,c,d=map(int,input().split())
if (a*b>=c*d):
    print(a*b)
else:
    print(c*d)