#coding: utf-8
from itertools import permutations
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
graph = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
P = permutations(r)
ans = float("inf")
for p in P:
    tmp = 0
    for i in range(R-1):
        tmp += graph[p[i]-1][p[i+1]-1]
    ans = min(ans, tmp)
print(ans) 
