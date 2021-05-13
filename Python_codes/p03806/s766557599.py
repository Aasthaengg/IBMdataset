n,ma,mb=map(int,input().split())
abc = [list(map(int,input().split())) for _ in range(n)]
suma = sum([abc[i][0] for i in range(n)])+1
sumb = sum([abc[i][1] for i in range(n)])+1
dp = [[[5000 for j in range(sumb)]for i in range(suma)]for k in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 0
for k in range(n):
    for i in range(suma):
        for j in range(sumb):
            if i>=abc[k][0] and j>=abc[k][1]:
                dp[k+1][i][j] = min(dp[k][i][j],dp[k][i-abc[k][0]][j-abc[k][1]]+abc[k][2])
            else:
                dp[k+1][i][j]=dp[k][i][j]

flag = 0
res = 5000
for i in range(1,500):
    if ma*i >=suma or mb*i >= sumb:
        break
    res = min(res,dp[n][ma*i][mb*i])
    flag = 1
if res != 5000:
    print(res)
else:
    print("-1")