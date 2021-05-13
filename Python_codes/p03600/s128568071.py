# -*- coding: utf-8 -*-
import sys 
from heapq import heappop,heappush
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
# INF = 10**31
cost = [[0]*(N+1) for _ in range(N+1)] 
tmp = [[0]*(N+1) for _ in range(N+1)] 
for i in range(N):
    A = list(map(int,readline().split()))
    for j in range(N):
        cost[i+1][j+1] = A[j]
        tmp[i+1][j+1] = A[j]
        

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                print(-1)
                sys.exit()
            if cost[i][k] and cost[k][j] and cost[i][j] == cost[i][k] + cost[k][j]:
                tmp[i][j] = 0

ans = sum([sum([c for c in row]) for row in tmp])
print(ans//2)