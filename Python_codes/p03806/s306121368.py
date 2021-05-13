#Mixing experiment
#dp[x][a][b]=Nこの商品のうちx番目まで見て、Aをaグラム、Bをbグラム得るために必要なお金の最小費用。
N,Ma,Mb=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(N)]
dp=[[[float("inf") for i in range(401)] for j in range(401)] for k in range(N+1)]
dp[0][0][0]=0
        
for i in range(N):
    a,b,c=D[i]
    for j in range(401):
        for k in range(401):
            if j>=a and k>=b:
                dp[i+1][j][k]=min(dp[i][j][k],dp[i][j-a][k-b]+c)
            else:
                dp[i+1][j][k]=dp[i][j][k]
ans=float("inf")
for i in range(1,401):
    if 0<Ma*i<=400 and 0<Mb*i<=400:
        ans=min(ans,dp[N][Ma*i][Mb*i])

if ans==float("inf"):
    print(-1)
else:
    print(ans)