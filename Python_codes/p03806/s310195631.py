import sys
input = sys.stdin.readline
n,ma,mb=map(int,input().split())
dp=[[[float("inf")]*500 for _ in range(500)] for i in range(n+1)]
dp[0][0][0]=0
for i in range(n):
    a,b,c=map(int,input().split())
    for j in range(450):
        for k in range(450):
            dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j][k])
            dp[i+1][j+a][k+b]=min(dp[i+1][j+a][k+b],dp[i][j][k]+c)
ans=float("inf")
i=1
#print(dp[-1])
while i*ma<450 and i*mb<450:
    ans=min(ans,dp[-1][ma*i][mb*i])
    i+=1
print(ans if ans!=float("inf") else -1)
