import sys
input = sys.stdin.readline
from scipy.sparse.csgraph import csgraph_from_dense, dijkstra

n,m = map(int,input().split())
A = [0]*m
B = [0]*m
C = [0]*m
for i in range(m) :
    a, b, c = map(int,input().split())
    A[i] = a-1
    B[i] = b-1
    C[i] = c

graph = [[0]*n for i in range(n)]

for i in range(m) :
    graph[A[i]][B[i]] = C[i]
    graph[B[i]][A[i]] = C[i]

graph = csgraph_from_dense(graph)
dist = dijkstra(graph)

ans = 0
for i in range(m) :
    if dist[A[i]][B[i]] != C[i] :
        ans += 1

print(ans)
