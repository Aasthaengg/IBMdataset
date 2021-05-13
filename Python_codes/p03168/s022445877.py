N=int(input())
p=list(map(float,input().split()))
dp=[0]*(N+1)
dp[0]=1
for i in range(0,N):
    for j in range(i+1,-1,-1):
        if(j!=0):
            dp[j]=dp[j-1]*p[i] + dp[j]*(1-p[i])
        else:
            dp[j]=dp[j]*(1-p[i])
ans=0
# print(dp)
for i in range(N//2+1,N+1):
    ans+=dp[i]
print(ans)