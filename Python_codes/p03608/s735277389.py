# -*- coding: utf-8 -*-
import sys 
from itertools import permutations
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
INF = 10**31

N, M, R = map(int, readline().split())
r = list(map(int,readline().split()))
len_r = len(r)
cost = [[INF]*(N+1) for i in range(N+1)]

for i in range(M):
    s, t, d = map(int,readline().split())
    cost[s][t] = d
    cost[t][s] = d
  
for i in range(N+1):
    cost[i][i] = 0

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if cost[i][k] != INF and cost[k][j] != INF: #costがINFのときその道はつながっていないから
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

ans = INF
for A in permutations(r,len_r):
    total = 0
    for i in range(len_r-1):
        s = A[i]
        t = A[i+1]        
        total += cost[s][t]
    ans = min(total,ans)
print(ans)