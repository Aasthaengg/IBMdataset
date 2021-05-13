N = int(input())
plist = list(map(float, input().split()))
dp = [[0 for i in range(N+1)] for j in range(N)]
dp[0][0], dp[0][1] = plist[0], 1-plist[0]
for i in range(1, N):
    p = plist[i]
    for j in range(i+1):
        dp[i][j] += dp[i-1][j]*p
        dp[i][j+1] += dp[i-1][j]*(1-p)
print(sum(dp[-1][0:(N+1)//2]))