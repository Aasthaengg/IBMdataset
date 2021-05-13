n,ma,mb = map(int,input().split())
L = []
sa = 0
sb = 0
for i in range(n):
    a,b,c = map(int,input().split())
    sa += a
    sb += b
    L.append([a,b,c])
dp = [[[10000 for i in range(sb+1)] for i in range(sa+1)] for i in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    a = L[i][0]
    b = L[i][1]
    c = L[i][2]
    for j in range(sa+1):
        for k in range(sb+1):
            if j-a >= 0 and k-b >= 0:
                dp[i+1][j][k] = min(dp[i][j-a][k-b]+c,dp[i+1][j][k],dp[i][j][k])
            else:
                dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])
k = max(ma,mb)
t = min(sa,sb)
cur = 1
ans = 10000
while k*cur <= t:
    ans = min(ans,dp[n][ma*cur][mb*cur])
    cur += 1
if ans == 10000:
    print(-1)
else:
    print(ans)
