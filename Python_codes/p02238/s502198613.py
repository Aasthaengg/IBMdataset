# -*- coding: utf-8 -*-
# 標準入力を取得
n = int(input())
G = {}
for _ in range(n):
    g = list(map(int, input().split()))
    G[g[0]] = g[2:]

# 求解処理
seen = [False for _ in range(n)]
ans = []


def dfs(v: int) -> None:
    seen[v - 1] = True
    ans.append(v)

    for w in G[v]:
        if not seen[w - 1]:
            dfs(w)

    ans.append(v)


while sum(seen) != n:
    v = seen.index(False)
    dfs(v + 1)

d = [-1 for _ in range(n)]
f = [-1 for _ in range(n)]

for i, a in enumerate(ans):
    if d[a - 1] == -1:
        d[a - 1] = i + 1
    else:
        f[a - 1] = i + 1

for id in range(n):
    print(id + 1, d[id], f[id])

