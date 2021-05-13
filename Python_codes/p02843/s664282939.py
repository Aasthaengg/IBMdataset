X=int(input())
dp=['']*(X+1)
for i in range(X+1):
    if i==0:
        dp[0]=1
    elif i<100:
        dp[i]=0
    else:
        if 1 in [dp[i-100],dp[i-101],dp[i-102],dp[i-103],dp[i-104],dp[i-105]]:
            dp[i]=1
        else:
            dp[i]=0
print(dp[X])