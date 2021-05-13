H,N=list(map(int,input().split()))
A=[tuple(map(int,input().split())) for _ in range(N)]

INF=10**9+7
dp=[INF]*(H+1)
dp[0]=0
for i in range(H):
    if dp[i]==INF:
        continue
    for j in range(N):
        a=A[j][0]
        b=A[j][1]
        k=min(H,i+a)
        dp[k]=min(dp[k], dp[i]+b)
print(dp[-1])