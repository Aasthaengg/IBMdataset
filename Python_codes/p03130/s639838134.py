#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

G=[[0]*4 for i in range(4)]
for i in range(3):
    a,b=map(int,input().split())
    a-=1;b-=1
    G[a].append(b)
    G[b].append(a)
visited=[0]*4
def dfs(node):
    visited[node]=1
    for gi in G[node]:
        if not visited[gi]:
            dfs(gi)
            return
dfs(0)
if all(visited):
    print("YES")
else:
    print("NO")
        
