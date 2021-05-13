N = int(input())
data = [[] for _ in range(N)]
for i in range(N):
    data[i] = [int(i) for i in input().split()]

#%%
dp = [[0] * 3 for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(3):
        temp = max(dp[i - 1][j - 1], dp[i - 1][j - 2])
        dp[i][j]= data[i - 1][j] + temp

ans = 0
for i in range(3):
    ans = max(ans, dp[N][i])

print(ans)
