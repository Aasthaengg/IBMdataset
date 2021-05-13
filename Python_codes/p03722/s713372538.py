def bellmanFord(edges):
    dist = [float('inf')] * N
    dist[0] = 0
    for _ in range(N-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    res = -dist[-1]
    neg = [False] * N
    for _ in range(N):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                neg[v] = True
            if neg[u]:
                neg[v] = True
    if neg[-1]:
        res = 'inf'
    return res

N, M = map(int, input().split())
A = [tuple()] * M
for i in range(M):
    a, b, c = map(int, input().split())
    A[i] = (a-1, b-1, -c)
ans = bellmanFord(A)
print(ans)