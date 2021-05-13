N = int(input())
MAXN = 1005
MAXV = MAXN*(MAXN-1)//2
to = [[]for _ in range(MAXV)]
id = [[0]*MAXN for _ in range(MAXN)]


def toId(i, j):
    return id[min(i, j)][max(i, j)]


visited = [False] * MAXV
calculated = [False] * MAXV
dp = [0] * MAXV


def dfs(v):
    if visited[v]:
        if not calculated[v]:
            return -1
        return dp[v]
    visited[v] = True
    dp[v] = 1
    for nv in to[v]:
        res = dfs(nv)
        if res == -1:
            return -1
        dp[v] = max(dp[v], res + 1)
    calculated[v] = True
    return dp[v]


a = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N-1):
        a[i][j] -= 1
vid = 0
for i in range(N):
    for j in range(N):
        if i < j:
            id[i][j] = vid
            vid += 1

# プレイヤーiの試合の依存関係の情報をグラフ化
for i in range(N):
    for j in range(N-1):
        a[i][j] = toId(i, a[i][j])
    for j in range(N-2):
        to[a[i][j+1]].append(a[i][j])
ans = 0

for i in range(vid):
    res = dfs(i)
    if res == -1:
        print(-1)
        exit()
    ans = max(ans, res)
print(ans)
