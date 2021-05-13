N = input().replace("\n", "")
L = len(N)
dp = [[0 for _ in range(2)] for i in range(L+1)]
dp[0][1] = 1
for i in range(L):
    n = int(N[i])
    dp[i+1][0] = min(dp[i][0]+n, dp[i][1]+(10-n))
    dp[i+1][1] = min(dp[i][0]+n+1, dp[i][1]+(9-n))
print(dp[L][0])
