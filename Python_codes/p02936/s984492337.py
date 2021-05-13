# 26

import sys

sys.setrecursionlimit(10**9)

n, q = map(int, input().split())
ans_l = [0] * n
graph = [[] for x in range(n)]

def dfs(v, p=-1):
    if p >= 0:
        ans_l[v] += ans_l[p]
    for i in range(len(graph[v])):
        _v = graph[v][i]
        if _v != p:
            dfs(_v, v)
        
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
for j in range(q):
    p, x = map(int, input().split())
    ans_l[p-1] += x
    
dfs(0)

print(*ans_l)