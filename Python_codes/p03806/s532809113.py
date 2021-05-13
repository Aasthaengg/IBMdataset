N,Ma,Mb = map(int,input().split())
dp = [[[10**9 for i in range(401)] for j in range(401)] for k in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    a,b,c = map(int,input().split())
    for j in range(401):
        for k in range(401):
            if j < a:
                dp[i][j][k] = dp[i-1][j][k]
            else:
                if k < b:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = min(dp[i-1][j][k],dp[i-1][j-a][k-b] + c)
m = max(Ma,Mb)
import math
n = math.floor(400 / m)
ans = 10**9
for i in range(1,400):
    x = Ma*i
    y = Mb*i
    if x > 400:
        break
    if y > 400:
        break
    ans = min(dp[N][x][y],ans)
if ans == 10**9:
    print(-1)
    quit()
print(ans)