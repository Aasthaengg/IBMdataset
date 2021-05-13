N, M = map(int, input().split())
edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort()

def bellmanford(n, edges, start):
    INF = float('inf')
    dist = [-INF] * (n+1) # dist[0]は使わない
    dist[start] = 0

    for i in range(n):
        for (pre, ne, weight) in edges:
            if dist[pre] != -INF and dist[pre] + weight > dist[ne]:
                dist[ne] = dist[pre] + weight
                if i == n-1 and ne == n:
                    return 'inf'
    return dist[n]

answer = bellmanford(N, edges, 1)
print(answer)