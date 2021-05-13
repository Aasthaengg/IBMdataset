n = int(input())
abc = [[] for i in range(n)]
for i in range(n):
    abc[i] = list(map(int, input().split()))
dp = [[0, 0, 0] for i in range(n)]
dp[0] = abc[0]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = dp[i-1][j-2] + abc[i][j] if dp[i-1][j-2] > dp[i-1][j-1] else dp[i-1][j-1] + abc[i][j]

print(max(dp[n-1]))