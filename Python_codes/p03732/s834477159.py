N,W = map(int,input().split())
wv = [list(map(int,input().split())) for i in range(N)]

dp = [[[-10**10]*(320) for j in range(100)] for i in range(N)]
#dp[i個までで][j個もって][余り部分kの重さ]の時の価値最大値

dp[0][0][0] = 0
dp[0][1][0] = wv[0][1]
for i in range(1,N):
    for j in range(100):
        for k in range(320):
            dp[i][j][k]=dp[i-1][j][k]#持たない
            if j-1>=0 and k+wv[0][0]-wv[i][0]>=0:#持つ
                dp[i][j][k]=max(dp[i][j][k],dp[i-1][j-1][k+wv[0][0]-wv[i][0]]+wv[i][1])
    
ans = 0
for j in range(100):
    for k in range(320):
        if j*wv[0][0]+k <= W:
            ans = max(ans,dp[N-1][j][k])


print(ans)