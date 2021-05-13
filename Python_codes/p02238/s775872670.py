def dfs(adj, s, d, f, now):
    now += 1
    d[s] = now
    for t in adj[s]:
        if t != s and f[t] < 0 and d[t] < 0:
            d, f, now = dfs(adj, t, d, f, now)
    now += 1
    f[s] = now
    return d, f, now


n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n):
    s = [int(x) for x in input().split()]
    u = s[0]
    for v in s[2:]:
        adj[u - 1].append(v - 1)
    adj[u - 1].sort()

d = [-1 for _ in range(n)]
f = [-1 for _ in range(n)]
now = 0
for s in range(n):
    if f[s] < 0:
        d, f, now = dfs(adj, s, d, f, now)

for i in range(n):
    print(str(i + 1) + " " + str(d[i]) + " " + str(f[i]))
