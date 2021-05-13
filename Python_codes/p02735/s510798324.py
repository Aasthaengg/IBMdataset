H,W=map(int,input().split())
S=[input() for _ in range(H)]
dp=[[10**9]*W for _ in range(H)]
if S[0][0]=='#':
    dp[0][0]=1
else:
    dp[0][0]=0
for i in range(H):
    for j in range(W):
        for di,dj in [(0,1),(1,0)]:
            ni=i+di
            nj=j+dj
            if ni<H and nj<W:
                if S[i][j]=='.' and S[ni][nj]=='#':
                    dp[ni][nj]=min(dp[ni][nj],dp[i][j]+1)
                else:
                    dp[ni][nj]=min(dp[ni][nj],dp[i][j])
print(dp[-1][-1])