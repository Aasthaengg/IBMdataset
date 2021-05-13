n,m=map(int,input().split())
a=set([int(input()) for j in range(m)])
dp=[0]*(n+1)
dp[0]=1
if not 1 in a:
    dp[1]=1
else:
    dp[1]=0
for i in range(n-1):
    if i+2 in a:
        dp[i+2]=0
    else:
        dp[i+2]=(dp[i+1]+dp[i])%(10**9+7)
print(dp[n])