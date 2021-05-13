H,W,K = map(int,input().split())
mod = 10**9+7
dp = [[0]*W for i in range(H+1)]

dp[0][0] = 1
for i in range(1,W):
    dp[0][i] = 0

for h in range(H):
    for w in range(W):
        
        for j in range((1<<W-1)):
            ok = True
            for k in range(1,W-1):
                if (j>>k)%2 == 1 and (j>>k-1)%2 == 1:
                    ok = False 
                    break
            if ok :
                #right
                if w < W-1 and (j>>w)%2 == 1:
                    dp[h+1][w+1] += dp[h][w]
                    dp[h+1][w+1] = dp[h+1][w+1]%mod
                #left
                elif w > 0 and (j>>w-1)%2 == 1:
                    dp[h+1][w-1] += dp[h][w]
                    dp[h+1][w-1] = dp[h+1][w-1]%mod
                else:
                    dp[h+1][w] += dp[h][w]
                    dp[h+1][w] = dp[h+1][w]%mod

print(dp[H][K-1]%mod)
            
             
