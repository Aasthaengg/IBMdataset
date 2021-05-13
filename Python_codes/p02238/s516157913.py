N = int(input())

E = [None] * (N+1)
for _ in range(N):
    u, k, *vs = list(map(int, input().split()))
    E[u] = vs

d = [0] * (N+1)
f = [0] * (N+1)
t = 0

def dfs(v):
    global t, d, f
    if d[v]:
        return
    t += 1
    d[v] = t
    for u in E[v]:
        dfs(u)
    t += 1
    f[v] = t

for v in range(1, N+1):
    dfs(v)

for v in range(1, N+1):
    print(v, d[v], f[v])

