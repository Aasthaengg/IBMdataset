H,W,K = map(int,input().split())
mod = 10**9+7
dp = [[0 for i in range(W)] for j in range(H+1)]
dp[0][0] = 1
dp_x = [[0,0] for i in range(W)]
dp_o = [[0,0] for i in range(W)]
dp_x[0][0] = 1
dp_x[0][1] = 1
for i in range(W-1):
    dp_x[i+1][0] = dp_x[i][0]+dp_x[i][1]
    dp_x[i+1][1] =dp_x[i][0]
dp_o[0][0] = 1
dp_o[0][1] = 0
for i in range(W-1):
    dp_o[i+1][0] = dp_o[i][0] + dp_o[i][1]
    dp_o[i+1][1] =dp_o[i][0]
dp_o = [sum(e) for e in dp_o]
dp_x = [sum(e) for e in dp_x]
dp_o = [1]+dp_o
dp_x = [1]+dp_x
if W == 1:
    print(1)
    exit()
for h in range(0,H):
    for w in range(W):
        if w == 0:
            dp[h+1][0] += dp[h][0]*dp_x[W-1-1]%mod
            dp[h+1][0] += dp[h][1]*dp_o[W-1-1]%mod
        elif w == W-1:
            dp[h+1][w] += dp[h][w]*dp_x[W-1-1]%mod
            dp[h+1][w] += dp[h][w-1]*dp_o[W-1-1]%mod
        else:
            #no connection
            dp[h+1][w] += dp[h][w]*dp_x[w-1]*dp_x[W-w-2]%mod
            #right connection
            dp[h+1][w] += dp[h][w+1]*dp_x[w-1]*dp_o[W-w-2]%mod
            #left connection
            dp[h+1][w] += dp[h][w-1]*dp_o[w-1]*dp_x[W-w-2]%mod
print(dp[H][K-1]%mod)
