dp=[0]*100
dp[0],dp[1]=2,1
for i in range(90):
    dp[i+2]=dp[i]+dp[i+1]
print(dp[int(input())])