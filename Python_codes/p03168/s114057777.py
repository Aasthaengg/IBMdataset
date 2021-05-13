N=int(input())
p=list(map(float,input().split()))

DP=[[0]*(N+1) for _ in range(N)]

DP[0][0]=1-p[0]
DP[0][1]=p[0]
for i in range(1,N):
    for j in range(i+2):
        if j==0:
            DP[i][j]=DP[i-1][j]*(1-p[i])
        else:
            DP[i][j]=DP[i-1][j-1]*p[i]+DP[i-1][j]*(1-p[i])
ans=sum(DP[N-1][(N+1)//2:])

print(ans)