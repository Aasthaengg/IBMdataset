n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

adj = [[] for _ in range(n)]
for a, b in ab:
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)


def dfs(s):
    d = [-1] * n
    p = [-1] * n
    d[s] = 0
    stack = [s]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                p[v] = u
                stack.append(v)

    return d, p


depth, par = dfs(0)
rev = (depth[n-1] - 1) // 2
root = n - 1
for _ in range(rev):
    root = par[root]

p = par[root]
adj[p].remove(root)
adj[root].remove(p)

depth, _ = dfs(n-1)
snuke = len([e for e in depth if e != -1])
fennec = n - snuke
if fennec > snuke:
    ans = "Fennec"
else:
    ans = "Snuke"
print(ans)

