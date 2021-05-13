N, M, P = map(int, input().split())
Edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    Edges.append([a, b, -(c - P)])


dist = [float('inf')] * N
dist[0] = 0

for i in range(2 * N):
    for fr, to, cost in Edges:
        if dist[to] > dist[fr] + cost:
            dist[to] = dist[fr] + cost
            if i >= N:
                dist[to] = -float('inf')


print(max(0, -dist[N - 1]) if -dist[N - 1] != float('inf') else -1)
