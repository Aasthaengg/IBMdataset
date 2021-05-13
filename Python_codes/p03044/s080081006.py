import sys
import copy
sys.setrecursionlimit(10**7)
def dfs(graph,v,dist_mod):
    color[v] = dist_mod
    for next_v,dist in graph[v]:
        if color[next_v] != -1:
            continue
        dfs(graph,next_v,(dist_mod+dist)%2)
n = int(input())
uvw = [list(map(int,input().split())) for _ in range(n-1)]
g = [[] for _ in range(n)]
color = [-1]*n
for i in range(n-1):
    g[uvw[i][0]-1].append([uvw[i][1]-1,uvw[i][2]])
    g[uvw[i][1]-1].append([uvw[i][0]-1,uvw[i][2]])
dfs(g,0,0)
for i in range(n):
    print(color[i])