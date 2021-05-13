n,ma,mb = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

dp = [[[10**10 for _ in range(430)] for _ in range(430)] for _ in range(45)]

dp[0][0][0] = 0

for i in range(n):
    a=l[i][0]
    b=l[i][1]
    c=l[i][2]
    for j in range(410):
        for k in range(410):
            dp[i+1][j][k] = min(dp[i+1][j][k] ,dp[i][j][k])
            dp[i+1][j+a][k+b] =min(dp[i+1][j+a][k+b], dp[i][j][k] +c)

ans=10**10
for j in range(1,410):
    for k in range(1,410):
        if ma*k == mb*j:
            ans=min(ans,dp[n][j][k])
if ans == 10**10:
    print(-1)
else:
    print(ans)