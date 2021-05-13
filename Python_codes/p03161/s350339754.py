INF = 10000
n,k = map(int,input().split())
stair = list(map(int,input().split()))
dp = [0] *n
for i in range(1,n):
    dp[i] = dp[i-1]+abs(stair[i]-stair[i-1])
    for j in range(1,k+1):
        if(i - j >= 0):
            # print(i,i-j)
            dp[i] = min(dp[i], dp[i-j]+abs(stair[i]-stair[i-j]))
        # print(dp)



print(dp[-1])
