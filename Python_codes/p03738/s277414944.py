#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf')
ans = 0 ;count = 0 ;pro = 1

a=int(input())
b=int(input())
if a>b:
    print("GREATER")
elif a<b:
    print("LESS")
else:
    print("EQUAL")