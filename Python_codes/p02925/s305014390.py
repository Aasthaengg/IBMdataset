import sys
sys.setrecursionlimit(1000000000)
n = int(input())
maxv = n*(n-1)//2
to = [[] for _ in range(maxv)]
vid = [[-1]*n for _ in range(n)]
def toId(i,j):
    if i > j: i,j = j,i
    return vid[i][j]
    
visited = [False]*maxv
calculated = [False]*maxv
dp = [0]*maxv
def dfs(v):
    if visited[v]:
        if not calculated[v]: return -1
        return dp[v]
    visited[v] = True
    dp[v] = 1
    for u in to[v]:
        res = dfs(u)
        if res == -1: return -1
        dp[v] = max(dp[v], res+1)
    calculated[v] = True
    return dp[v]

a = [[int(i)-1 for i in input().split()] for _ in range(n)]
v = 0
for i in range(n):
    for j in range(i+1,n):
        vid[i][j] = v
        v += 1
for i in range(n):
    for j in range(n-1): a[i][j] = toId(i,a[i][j])
    for j in range(n-2): to[a[i][j+1]].append(a[i][j])
ans = 0
for i in range(maxv):
    res = dfs(i)
    if res == -1:
        print(-1)
        exit()
    ans = max(ans, res)
print(ans)