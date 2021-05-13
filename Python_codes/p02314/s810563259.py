# DPL 1 A

def solve():
    INF = 1e+9
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    dp = [[0]*(n+1) for _ in range(m+1)]
    for j in range(n+1):
        dp[0][j] = INF

    for i in range(1, m+1):
        for j in range(1, n+1):
            jj = j - c[i-1]
            if jj < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][jj] + 1)

    print(dp[-1][-1])


if __name__ == "__main__":
    solve()

