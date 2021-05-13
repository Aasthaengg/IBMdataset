n,Ma, Mb = map(int, input().split())
dp=[[[1000000]*510 for i in range(510)] for j in range(n+1)]
dp[0][0][0]=0
for i in range(1,n+1):
    a, b, c = map(int, input().split())
    for j in range(410):
        for k in range(410):
            dp[i][j][k]=min(dp[i-1][j][k], dp[i][j][k])
            p=j+a
            q=k+b
            dp[i][p][q]=min(dp[i][p][q], dp[i-1][j][k]+c)
ans=1000000
for i in range(1, 410//max(Ma, Mb)+1):
    ans=min(dp[n][i*Ma][i*Mb], ans)
if ans==1000000:
    print(-1)
else:
    print(ans)