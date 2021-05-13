#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1
sys.setrecursionlimit(10**6)
n,U,V = map(int,input().split())
U-=1;V-=1
G = [[] for i in range(n)]
for i in range(n-1):
  a,b = map(int,input().split())
  a-=1;b-=1
  G[a].append(b)
  G[b].append(a)
Aokidis = [0]*n
Takahashidis = [0]*n
def dfs(node,dis,TorA,pre):
  if TorA == "Takahashi":Takahashidis[node] = dis
  else:Aokidis[node] = dis
  for vi in G[node]:
    if vi == pre:continue
    dfs(vi,dis+1,TorA,node)
dfs(U,0,"Takahashi",-1)
dfs(V,0,"",-1)
for i in range(n):
  if Takahashidis[i] <= Aokidis[i]:
    ans = max(ans,Aokidis[i]-1)
print(ans)