n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

C = list(map(int, input().split()))
C.sort(reverse=True)

order = []
par = [-1]*n
s = []
visit = [-1]*n
s.append(0)
visit[0] = 0
while s:
    v = s.pop()
    order.append(v)
    for u in g[v]:
        if u == par[v]:
            continue
        par[u] = v
        s.append(u)

order.reverse()
ans = [0]*n
m = 0
for v in order:
    ans[v] = C.pop()
    if par[v] != -1:
        m += ans[v]
print(m)
print(*ans)