from sys import setrecursionlimit


def encode(i, j):
    if i < j:
        i, j = j, i
    return i * (i - 1) // 2 + j + 1


def dfs(v):
    if visited[v] == 2:
        return dp[v]
    visited[v] = 1
    for nv in g[v]:
        if visited[nv] == 1:
            print(-1)
            exit()
        dp[v] = max(dp[v], dfs(nv) + 1)
    visited[v] = 2
    return dp[v]


setrecursionlimit(10 ** 6)
N = int(input())
GAMES_CNT = N * (N - 1) // 2
g = [[] for _ in range(GAMES_CNT + 1)]
for i in range(N):
    orig = 0
    for j in map(lambda x: int(x) - 1, input().split()):
        dest = encode(i, j)
        g[orig].append(dest)
        orig = dest
dp = [0] * (GAMES_CNT + 1)
visited = [0] * (GAMES_CNT + 1)
print(dfs(0))
