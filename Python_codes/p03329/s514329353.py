n=int(input())
a=[6**i for i in range(10)]+[9**i for i in range(10)]
dp=list(range(10**5+1))
dp[1]=1
for i in range(n):
    for j in a:
        if i+j<10**5+1:
            dp[i+j]=min(dp[i+j],dp[i]+1)
print(dp[n])