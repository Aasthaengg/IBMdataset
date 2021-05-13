#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,k=map(int,input().split())
G=[]
for i in range(2,n+1):
    G.append((1,i))
s=(n-1)*(n-2)//2
if k > s:
    print(-1); exit()
for i in range(2,n):
    for j in range(i+1,n+1):
        if count < s-k:
            G.append((i,j))
            count += 1

print(len(G))
for gi in G:
    print(*gi)



