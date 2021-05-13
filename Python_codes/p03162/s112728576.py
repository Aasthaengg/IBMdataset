

INF = float('inf')


def tc():
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]

    # dp[i][j]: max happiness on day i+1 if you do act j (a, b, c)
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = a[0]

    # since from one stone you can go to many
    # try using push dp instead of pull
    for i in range(n - 1):
        dp[i + 1][0] = max(dp[i][1], dp[i][2]) + a[i + 1][0]
        dp[i + 1][1] = max(dp[i][0], dp[i][2]) + a[i + 1][1]
        dp[i + 1][2] = max(dp[i][0], dp[i][1]) + a[i + 1][2]

    print(max(dp[-1]))


tc()
