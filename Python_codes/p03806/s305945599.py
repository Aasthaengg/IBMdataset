n,ma,mb = map(int,input().split())
a = []
b = []
c = []
for i in range(n):
    aa,bb,cc = map(int,input().split())
    a.append(aa)
    b.append(bb)
    c.append(cc)

inf = 10**18
dp = [[[inf]*(411) for j in range(411)] for i in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 0
for i in range(n):
    for j in range(400):
        for k in range(400):
            if dp[i][j][k] == inf:continue
            dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])
            dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]],dp[i][j][k]+c[i])

ans = 10**18
for j in range(1,401):
    for k in range(1,401):
        if ma*k == mb*j:
            ans = min(ans,dp[n][j][k]) 
if ans == 10**18:
    print(-1)
else:
    print(ans)



