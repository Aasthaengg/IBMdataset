# -*- coding: utf-8 -*-
import sys 
sys.setrecursionlimit(10**6)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M = map(int,readline().split())
road = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for i in range(M):
    x,y = map(int,readline().split())
    road[x].append(y)
    road[y].append(x)
  
def dfs(v,prev):
    for x in road[v]:
        if x == prev:
            continue
        if visit[x] != 0:
            continue
        visit[x] = 1
        dfs(x,v)
    return 

count = 0     
for i in range(1,N+1):
    if visit[i] == 0:
        dfs(i,-1)
        count += 1

print(count-1)