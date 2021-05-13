N, M = map(int, input().split())
LRD = [list(map(int, input().split())) for _ in range(M)]

G = [{} for _ in range(N+1)]
for L, R, D in LRD:
    G[L][R] = D
    G[R][L] = -D

visited = [False] * (N+1)
dist = [0] * (N+1)


def dfs(v):
    q = [v]
    while q:
        cu = q.pop()
        for nx, d in G[cu].items():
            if visited[nx]:
                if dist[nx] != dist[cu] + d:
                    # print(nx, dist[nx], cu, dist[cu], d)
                    print('No')
                    exit()
            else:
                visited[nx] = True
                dist[nx] = dist[cu] + d
                q.append(nx)
    return True


for n in range(1, N+1):
    if not visited[n]:
        dfs(n)
print('Yes')
