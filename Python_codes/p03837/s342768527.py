import sys
N, M = map(int, sys.stdin.readline().strip().split())
 
def warshall_floyd(d):
    # d[i][j]: iからjへの最短距離
    for k in range(size_v):
        for i in range(size_v):
            for j in range(size_v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
 
edges = []
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    edges.append((a, b, c))
#print(graph)
 
size_v = N + 1
dist=[[float("inf")] * size_v for i in range(size_v)] 
 
for a, b, c in edges:
    dist[a][b] = c
    dist[b][a] = c
for i in range(size_v):
    dist[i][i] = 0
 
dist = warshall_floyd(dist)
#print(dist)
  
answer_set = set()
for a, b, c in edges:
    if dist[a][b] == c:
        answer_set.add((a, b, c))
    
print(M - len(answer_set))