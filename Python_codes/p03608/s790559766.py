import itertools

def warshall_floid(graph: list) -> list:
    """warshall-floid法: 各頂点から各頂点への最短距離を求める
    計算量: O(V^3)
    """
    n = len(graph)
    INF = 10 ** 18
    dp = [[INF] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n):
        for j, cost in graph[i]:
            dp[i][j] = cost

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

n, m, r = map(int, input().split())
r = list(map(int, input().split()))
info = [list(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
for i in range(m):
    a, b, cost = info[i]
    a -= 1
    b -= 1
    graph[a].append((b, cost))
    graph[b].append((a, cost))
dp = warshall_floid(graph)

ans = 10 ** 18
for ptn in itertools.permutations(r):
    tmp = 0
    for i in range(1, len(ptn)):
        tmp += dp[ptn[i] - 1][ptn[i - 1] - 1]
    ans = min(ans, tmp)
print(ans)