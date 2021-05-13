inf = float('inf')

N, M = map(int,input().split())
edges = []
for _ in range(M):
    a, b, c = map(int,input().split())
    a -= 1; b-= 1
    edges.append((a, b, -c))

dist = [inf] * N
dist[0] = 0
for _ in range(N-1):
    for v, nv, w in edges:
        if dist[nv] > dist[v] + w:
            dist[nv] = dist[v] + w

is_update = [False] * N
for _ in range(N):
    for v, nv, w in edges:
        if dist[nv] > dist[v] + w:
            dist[nv] = dist[v] + w
            is_update[nv] = True
        if is_update[v] is True:
            is_update[nv] = True

if is_update[N-1] is True:
    ans = "inf"
else:
    ans = -dist[N-1]

print(ans)