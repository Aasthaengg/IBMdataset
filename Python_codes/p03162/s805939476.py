N = int(input())
dp = [[0]*N for _ in range(3)] #dp[k][i] i日目にactivity k を実施する

dp[0][0],dp[1][0],dp[2][0] = map(int,input().split())
for i in range(1,N):
    act= list(map(int,input().split()))
    for k in range(3):
        dp[k][i] = max(dp[(k+1)%3][i-1],dp[(k+2)%3][i-1])+act[k%3]
ans = 0
for k in range(3):
    ans = max(ans,dp[k][-1])
print(ans)
    

