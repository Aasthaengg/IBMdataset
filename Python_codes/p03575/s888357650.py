N, M = map(int, input().split())
ab = [[] for _ in range(N)]
abl = []
for _ in range(M):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)
    abl.append([a-1, b-1])


# DFS
def dfs(v):
    global da, db
    if tf[v]:
        return
    tf[v] = True
    for nv in ab[v]:
        if v == da and nv == db:
            continue
        if v == db and nv == da:
            continue
        dfs(nv)
    return


# 辺を１本ずつ抜いていってそれぞれDFS
ans = 0
for i in range(M):
    da, db = abl[i]
    tf = [False for _ in range(N)]
    dfs(0)
    if not all(e for e in tf):
        ans += 1
print(ans)