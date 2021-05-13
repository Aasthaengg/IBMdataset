p,q,r=map(int,input().split())
dp=[0]*2
dp[0]=min(p,q)
dp[1]=min(max(q,p),r)
print(dp[1]+dp[0])