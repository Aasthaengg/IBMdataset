n=int(input())
P=map(float,input().split())
dp=[0]*(n+2)
dp[0]=1
for p in P:
    for i in range(n,-1,-1):
        dp[i]=dp[i]*p+dp[i-1]*(1-p)
print(sum(dp[:n//2+1]))