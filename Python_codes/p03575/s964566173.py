def dfs(cur):
    visited[cur] = 1
    for nx in range(n):
        if G[cur][nx] == 0:
            continue
        if visited[nx]:
            continue
        dfs(nx)


n, m = map(int, input().split())
G = [[0]*n for _ in range(n)]
ab = []
for i in range(m):
    a, b = map(int, input().split())
    ab.append((a-1, b-1))
    G[a-1][b-1] = G[b-1][a-1] = 1
ans = 0
for a, b in ab:
    G[a][b] = G[b][a] = 0
    visited = [0]*n
    dfs(0)
    if not all(visited):
        ans += 1
    G[a][b] = G[b][a] = 1

print(ans)