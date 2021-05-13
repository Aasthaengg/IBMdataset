import sys
sys.setrecursionlimit(200000)

n = int(input())
 
G = {}
for i in range(n):
    G.update({i: []})
 
for i in range(n - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append([v - 1, w % 2])
    G[v - 1].append([u - 1, w % 2])
 
color = [-1 for i in range(n)]
 
def dfs(graph, v, c):
    color[v] = c
    
    for next_v in graph[v]:
        dis = next_v[1]
        if color[next_v[0]] != -1:
            continue
        
        if dis == 0:
            n_c = c
        elif dis == 1:
            n_c = 1 - c
        
        dfs(graph, next_v[0], n_c)
 
dfs(G, 0, 0)
[print(i) for i in color]