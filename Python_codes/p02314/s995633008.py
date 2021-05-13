INF = 10**10
N,M = map(int,input().split())
Coins = list(map(int,input().split()))
Coins.sort()
# DP[x種類目までのコイン][n円を支払う]
# index1 0,1(1種類め),...(n種類め)
# index2 0円,1円,2円... 
# DP[m+1][n+1]で作成
DP = [ [INF]*(N+1) for _ in range(M+1) ]

# 0円の場合の支払いに必要な枚数は 0
for i in range(1,M+1):
    DP[i][0] = 0

# 1円のみで支払う場合
for i in range(1,N+1):
    DP[1][i] = i
# 2種類め以降を使う場合
for m in range(2,M+1):
    for n in range(1,N+1):
        # 支払うのは n円
        # 1枚 c円
        c = Coins[m-1]
        if n >= c:
            DP[m][n] = min(DP[m][n],DP[m][n-c] + 1)
        DP[m][n] = min(DP[m][n],DP[m-1][n])

print(DP[M][N])
