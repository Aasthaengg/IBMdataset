# 両方から到達出来ないものに関する辺を無視してベルマンフォード
import sys
sys.setrecursionlimit(10**6)
n, m, p = map(int, input().split())
edges = []
to = [[] for _ in range(n)]
ot = [[] for _ in range(n)]
reachable_from_1 = [False] * n
reachable_to_n = [False] * n
ok = [False] * n
INF = float('inf')


def dfs(v):
    if reachable_from_1[v]:
        return
    reachable_from_1[v] = True
    for nv in to[v]:
        dfs(nv)


def rdfs(v):
    if reachable_to_n[v]:
        return
    reachable_to_n[v] = True
    for nv in ot[v]:
        rdfs(nv)


for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c -= p
    c = -c
    edges.append((a, b, c))
    to[a].append(b)
    ot[b].append(a)
dfs(0)
rdfs(n - 1)
for i in range(n):
    ok[i] = reachable_from_1[i] and reachable_to_n[i]
d = [INF] * n
d[0] = 0
upd = True
step = 0
while upd:
    upd = False
    for e in edges:
        frm, to, cost = e
        if not ok[frm]:
            continue
        if not ok[to]:
            continue
        nd = d[frm] + cost
        if nd < d[to]:
            d[to] = nd
            upd = True
    step += 1
    if step > n:
        print(-1)
        exit()
ans = -d[n - 1]
ans = max(0, ans)
print(ans)
