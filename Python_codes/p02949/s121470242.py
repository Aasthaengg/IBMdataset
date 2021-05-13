import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
edges = [None] * M
for i in range(M):
    A, B, C = map(int, input().split())
    edges[i] = (A, B, P-C)

dist = [float('inf')] * (N+1)
dist[1] = 0
for i in range(N-1):
    for u, v, weight in edges:
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
negative = [False] * (N+1)
for i in range(N):
    for u, v, weight in edges:
        if negative[u]:
            negative[v] = True
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            negative[v] = True
print(max(-dist[N], 0) if not negative[N] else -1)
