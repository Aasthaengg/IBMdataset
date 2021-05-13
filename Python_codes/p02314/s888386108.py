n, m = map(int, input().split())
price = list(map(int, input().split()))

#dp[i][j]をi番目まででj支払える最小枚数
dp = [[float("inf")] * (n+1) for _ in range(m+1)]

for _ in range(m+1):
    dp[_][0] = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if j >= price[i-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-price[i-1]]+1)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])

