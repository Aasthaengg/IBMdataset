# coding: utf-8
N=int(input())
A=list(map(int,input().split()))
INF=10**9
dp=[[-INF for i in range(N+1)] for j in range(N+1)]
dp[0][0]=0
AI=[]

for i in range(N):
    AI.append([A[i],i+1])
    
AI.sort()
AI.reverse()

for i in range(1,N+1):
    a=AI[i-1][0]
    I=AI[i-1][1]
    for j in range(N+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+abs(I-(N+1-i))*a
        elif j==i:
            dp[i][j]=dp[i-1][j-1]+abs(I-j)*a
        else:
            dp[i][j]=max(dp[i-1][j-1]+abs(I-j)*a,dp[i-1][j]+abs(I-(N+1-(i-j)))*a)
ans=0
for i in range(N+1):
    ans=max(ans,dp[N][i])

print(ans)