N,W = map(int,input().split())
WV = [list(map(int,input().split())) for _ in [0]*N]

#dp[i][n:入れた数][dW:w1からの差分の合計]
dp = [[[0]*(3*N+1) for _ in [0]*(N+1)] for _ in [0]*(N+1)]
w0 = WV[0][0]
for i,wv in enumerate(WV,1):
    w,v = wv
    w -= w0
    for n in range(1,i+1):
        for dW in range(3*N+1):
            if n*w0 + dW > W:break
            if w>dW:
                dp[i][n][dW] = dp[i-1][n][dW]
                continue
            dp[i][n][dW] = max(dp[i-1][n][dW],dp[i-1][n-1][dW-w]+v)
print(max(max(row) for row in dp[-1]))