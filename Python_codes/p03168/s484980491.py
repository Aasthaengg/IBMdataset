import sys
input=sys.stdin.readline

N=int(input())
p=list(map(float,input().split()))

dp=[[0]*(N+1)for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i==0 and j==0:
            dp[i][j]=1
        elif j==0:
            dp[i][j]=dp[i-1][j]*(1-p[i-1])
        elif i>=j:
            dp[i][j]=(dp[i-1][j]*(1-p[i-1]))+(dp[i-1][j-1]*p[i-1])

ans=0
for j in range(((N//2)+1),N+1):
    ans+=dp[N][j]
print(ans)