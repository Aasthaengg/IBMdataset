n, m = map(int, input().split())
li_c = list(map(int, input().split()))

INF = 10**7
dp = [INF]*(50010)
dp[0] = 0
dp[1] = 1
# dp[i] : i 円支払う時の最小の枚数
for i in range(50001):
    for coin in li_c:
        if i+coin<50010:
            dp[i+coin] = min(dp[i]+1, dp[i+coin])
print(dp[n])


