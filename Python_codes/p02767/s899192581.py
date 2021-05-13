N=int(input())
array=list(map(int,input().split()))

X=[0]
for i in array:
    X.append(i)

INF=10000000

dp=[[INF for j in range(100+1)] for j in range(N+1)]

for i in range(100+1):
    dp[0][i]=0

for i in range(1,N+1):
    for j in range(1,100+1):
        dp[i][j]=min(dp[i][j],dp[i-1][j]+(X[i]-j)**2)
        
ans=INF
for i in range(1,100+1):
    ans=min(ans,dp[N][i])

print(ans)