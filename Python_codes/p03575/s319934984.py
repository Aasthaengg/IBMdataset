N, M = map(int, input().split())
G = [[] for _ in range(N)]
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    edges.append([a - 1, b - 1])

def dfs(u, seen, e):
    seen[u] = True
    for v in G[u]:
        if seen[v] == True:
            continue
        if [u, v] == e or [v, u] == e:
            continue
        dfs(v, seen, e)

ans = 0
for e in edges:
    seen = [False] * N
    dfs(e[0], seen, e)
    if seen[e[1]] == False:
        ans += 1

print(ans)