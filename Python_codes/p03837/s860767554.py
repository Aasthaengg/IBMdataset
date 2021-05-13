from copy import deepcopy


def floyd_warshall(dist):
    v = len(dist)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

INF = 10**9
N, M = map(int, input().split())
G = [[INF] * N for _ in range(N)]
for i in range(N):
    G[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = G[b][a] = c
dist = deepcopy(G)
floyd_warshall(dist)
used = set()
for i in range(N-1):
    checked = set()
    for j in range(i+1, N):
        stack = [j]
        while stack:
            v = stack.pop()
            if v in checked:
                continue
            checked.add(v)
            for k in range(N):
                if v == k:
                    continue
                if G[k][v] == INF:
                    continue
                if dist[i][v] == dist[i][k] + G[k][v]:
                    stack.append(k)
                    used.add((k, v) if k < v else (v, k))
print(M - len(used))
