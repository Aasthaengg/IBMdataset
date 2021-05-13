n, m = map(int, input().split())
l = []
edges = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    l.append([a - 1, b - 1])
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
def dfs(cur, a, b):
    if visited[cur] == 1:
        return None
    visited[cur] = 1
    for v in edges[cur]:
        if v != b or cur != a:
            dfs(v, a, b)
ans = 0
for i in l:
    i, j = i[0], i[1]
    visited = [0 for i in range(n)]
    dfs(i, i, j)
    if visited[j] == 0:
        ans += 1
print(ans)