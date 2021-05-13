import sys
sys.setrecursionlimit(10000000)
N, M = map(int, input().split())
ki = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ki[a-1].append(b-1)
    ki[b-1].append(a-1)
tf = [False for _ in range(N)]

# DFS
def dfs(v):
    global eda
    tf[v] = True
    eda += 1
    for nv in set(ki[v]):
        if not tf[nv]:
            dfs(nv)

ans = 0
for i in range(N):
    if not tf[i]:
        eda = 0
        dfs(i)
        ans = max(ans, eda)
print(ans)