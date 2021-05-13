R,C,K=map(int,input().split())
rcv = [[0]*C for _ in range(R)]
for i in range(K):
    r,c,v = map(int,input().split())
    rcv[r-1][c-1]=v

dp = [[[0]*C for _ in range(R)] for _ in range(0,4)]

dp[1][0][0]=rcv[0][0]

#左端を縦に
j=0
for i in range(1,R):
    if rcv[i][j]==0:
        dp[0][i][j] = max(dp[r][i-1][j] for r in range(4))
    else:
        dp[0][i][j] = max(dp[r][i-1][j] for r in range(4))
        dp[1][i][j] = max(dp[r][i-1][j] for r in range(4))+rcv[i][j]

#上端を右に 
i=0
for j in range(1,C):
    if rcv[i][j]==0:
        for r in range(4):#左から引き継ぐだけ
            dp[r][i][j] = dp[r][i][j-1]
    else:
        dp[0][i][j] = dp[0][i][j-1]
        for r in range(1,4):
            dp[r][i][j] = max(dp[r][i][j-1] , dp[r-1][i][j-1]+rcv[i][j])

for i in range(1,R):
    for j in range(1,C):
        if rcv[i][j]==0:#左から引き継ぐか、上から引き継いでカウントキャンセル
            dp[0][i][j] = max(dp[0][i][j-1],
                              max(dp[r][i-1][j] for r in range(4) ) )
            for r in range(1,4):#左から引き継ぐだけ
                dp[r][i][j] = dp[r][i][j-1]
        else:
            dp[0][i][j] = max(dp[0][i][j-1],
                              max(dp[r][i-1][j] for r in range(4) ) )
            dp[1][i][j] = max(dp[1][i][j-1], dp[0][i][j-1]+rcv[i][j],
                              max(dp[r][i-1][j] for r in range(4) )+rcv[i][j] )
            for r in [2,3]:#左からのみ
                dp[r][i][j] = max(dp[r][i][j-1], dp[r-1][i][j-1]+rcv[i][j] )
print(max( dp[i][-1][-1] for i in range(4)) )