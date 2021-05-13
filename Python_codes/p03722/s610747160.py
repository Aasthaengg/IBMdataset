inf = float("inf")
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))
d = [-inf] * N
d[0] = 0
for i in range(N):
    for a, b, c in edges:
        if d[b] < d[a] + c:
            d[b] = d[a] + c
for i in range(N):
    for a, b, c in edges:
        if d[b] < d[a] + c:
            d[b] = inf
print(d[N - 1])
