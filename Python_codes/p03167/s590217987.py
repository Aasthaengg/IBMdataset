import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    m, n = map(int, input().split())
    grid = [input() for _ in range(m)]
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    D = [(1, 0), (0, 1)]
    for i in range(m):
        for j in range(n):
            for di, dj in D:
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] == '#':
                    continue
                dp[ni][nj] += dp[i][j]
                if dp[ni][nj] >= MOD:
                    dp[ni][nj] -= MOD

    print(dp[m - 1][n - 1])
resolve()