n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n-1):
        a[i][j] -= 1

MAXN = 1005
MAXV = MAXN*(MAXN-1)//2

to = [[] for _ in range(MAXV)]
# 頂点番号
id = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
def toID(i, j):
    if i > j:
        i, j = j, i
    return id[i][j]

# 頂点番号のラベリング
V = 0
for i in range(n):
    for j in range(n):
        if i < j:
            id[i][j] += V
            V += 1

# aを、頂点番号に書き換え、試合の依存関係を表す辺を張る(辺の向きは逆にする)
for i in range(n):
    for j in range(n-1):
        a[i][j] = toID(i, a[i][j])
    for j in range(n-2):
        to[a[i][j+1]].append(a[i][j])

# dfsする
visited = [False for _ in range(MAXV)]
calculated = [False for _ in range(MAXV)] # loop 検出用
dp = [0 for _ in range(MAXV)] # max length of path from v
def dfs(v):
    if visited[v]:
        if not calculated[v]:
            return -1
        return dp[v]
    visited[v] = True
    dp[v] = 1
    for u in to[v]:
        res = dfs(u)
        if res == -1:
            return -1
        dp[v] = max(dp[v], res+1)
    calculated[v] = True
    return dp[v]

ans = 0
ok = True
for i in range(V):
    res = dfs(i)
    if res == -1:
        ok = False
        break
    ans = max(ans, res)
if ok:
    print(ans)
else:
    print(-1)