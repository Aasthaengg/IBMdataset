n, m = map(int, input().split())
dp = [0] * n
indeg = [0] * n
to = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    to[x].append(y)
    indeg[y] += 1
avail = list(filter(lambda i: indeg[i] == 0, range(n)))
while avail:
    u = avail.pop()
    for v in to[u]:
        dp[v] = max(dp[v], dp[u] + 1)
        indeg[v] -= 1
        if indeg[v] == 0:
            avail.append(v)
print(max(dp))