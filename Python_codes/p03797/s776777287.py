#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf')
ans = 0 ;count = 0 ;pro = 1

n,m=map(int,input().split())
k=min(m//2,n)
m-=2*k;n-=k
count+=k
# print(n,m,k)
count+=m//4
print(count)