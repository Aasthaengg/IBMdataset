n=int(input())
dp=[0]*100
dp[0]=2
dp[1]=1
for i in range(90):
    dp[i+2]=dp[i]+dp[i+1]
print(dp[n])