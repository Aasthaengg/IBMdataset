#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, fractions
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = count = 0

a,b,h=[int(input()) for i in range(3)]
print((a+b)*h//2)