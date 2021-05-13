#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
A=list(map(int,input().split()))
K=sum(A)/n
ans=(inf,0)
for i ,ai in enumerate(A):
    if ans[0]>abs(K-ai):
        ans=(abs(K-ai),i)
print(ans[1])