n,m=map(int,input().split())
C=list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=1

for i in range(m):
    for j in range(n+1):
        if dp[j]!=0:
            if j+C[i]<=n:
                if dp[j+C[i]]==0:
                    dp[j+C[i]]=dp[j]+1
                else:
                    dp[j+C[i]]=min(dp[j]+1,dp[j+C[i]])
    #print(dp)
print(dp[n]-1)
