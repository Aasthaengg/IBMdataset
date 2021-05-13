N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
use=[0,2,5,5,4,5,6,3,7,6]
dp=[-1]*(N+1)
dp[0]=0
for i in range(N+1):
    for k in A:
        if i+use[k]<=N:
            dp[i+use[k]]=max(dp[i]+1,dp[i+use[k]])
ans=""
now=N
for i in range(dp[N]):
    for k in A:
        if now-use[k]>=0:
            if dp[now-use[k]]==dp[now]-1:
                ans+=str(k)
                now-=use[k]
                break
print(ans)