h,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
inf=10**9
dp=[inf]*(h+10**5)
dp[0]=0
#dp[i]=モンスターの体力をi減らすのに魔力が最低でいくつ必要か
for i in range(h):
    for a,b in l:
        dp[i+a]=min(dp[i+a],dp[i]+b)
ans=10**9
for i in range(10**5):
    ans=min(ans,dp[i+h])
print(ans)