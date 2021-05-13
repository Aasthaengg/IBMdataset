n = int(input())
p = list(map(float, input().split()))
dp = [[0]*(n+1) for _ in range(len(p)+1)]
dp[1][0] = (1-p[0])
dp[1][1] = p[0]
for i in range(1, n):
    for j in range(i+2):
        if j == 0: dp[i+1][0] = dp[i][0]*(1-p[i])
        else: dp[i+1][j] = dp[i][j-1]*p[i]+dp[i][j]*(1-p[i])
print(sum(dp[-1][-(-n//2):]))