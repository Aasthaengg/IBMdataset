import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, -c))
dist = [float('inf')] * (N+1)
dist[1] = 0
for _ in range(N-1):
    for u, v, weight in edges:
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
negative = [False] * (N+1)
for _ in range(N):
    for u, v, weight in edges:
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            negative[v] = True
print('inf' if negative[N] else -dist[N])