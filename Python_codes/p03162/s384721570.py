n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
a,b,c = [list(i) for i in zip(*l)]
dp = [[0,0,0] for i in range(n+1)]
for i in range(n):
    dp[i+1][0] = max(dp[i][1]+a[i],dp[i][2]+a[i])
    dp[i+1][1] = max(dp[i][0]+b[i],dp[i][2]+b[i])
    dp[i+1][2] = max(dp[i][0]+c[i],dp[i][1]+c[i])
print(max(dp[-1]))