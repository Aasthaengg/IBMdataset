#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a = b = c = 0
n = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
for i,pi in enumerate(P):
    if pi <= A:
        a += 1
    elif A+1 <= pi <= B:
        b += 1
    else:
        c += 1
print(min(a,b,c))
