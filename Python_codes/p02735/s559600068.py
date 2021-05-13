H,W=map(int,input().split())
S=tuple(tuple(input()) for _ in range(H))

dp=[[10**9 for _ in range(W)] for __ in range(H)]
dp[0][0]=int(S[0][0]!='.')
for i in range(H):
    for j in range(W):
        for di,dj in [[0,1],[1,0]]:
            ni=i+di
            nj=j+dj
            if 0<=ni<H and 0<=nj<W:
                WB=S[i][j]=='.' and S[ni][nj]=='#'
                dp[ni][nj]=min(dp[ni][nj],dp[i][j]+int(WB))
print(dp[-1][-1])