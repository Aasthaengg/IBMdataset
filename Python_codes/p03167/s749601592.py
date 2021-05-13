H,W=list(map(int, input().split()))
G=[['#' for j in range(W+1)]]
for i in range(H):
    G.append(['#']+(list(input())))
# print(G)
C=10**9+7

# dp[i][j]:(i,j)に辿り着く場合の数
# 左や上に壁がないときその場合の数を加算
# 上の行と左の列に壁'#'を追加することにする
# Gだけ1-indexなことに注意

dp=[[0 for j in range(W)] for i in range(H)]
dp[0][0]=1

for i in range(H):
    for j in range(W):
        if G[i+1][j+1]=='#':
            continue
        if G[i][j+1]!='#':
            dp[i][j]+=dp[i-1][j]
            dp[i][j]%=C
        if G[i+1][j]!='#':
            dp[i][j]+=dp[i][j-1]
            dp[i][j]%=C
    # print(dp[i])
print(dp[H-1][W-1])