n=int(input())
dp=[10**18]*(n+1)
dp[n]=0
for i in range(5,0,-1):
    for j in range(n,0,-1):
        if j-9**i>=0:
            dp[j-9**i]=min(dp[j-9**i],dp[j]+1)

for i in range(6,-1,-1):
    for j in range(n,0,-1):
        if j-6**i>=0:
            dp[j-6**i]=min(dp[j-6**i],dp[j]+1)
pass
print(dp[0])