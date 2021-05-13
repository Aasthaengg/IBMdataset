h,w = map(int,input().split())
s = [input()for _ in range(h)]
dp = [[10**8]*(w+1) for _ in range(h+1)]
dp[0][0] = 0
for i in range(h):
    for j in range(w): 
        if s[i][j] == '.':
            if i+1 < h and s[i+1][j] == '#':dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
            else:dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            if j+1 < w and s[i][j+1] == '#':dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
            else:dp[i][j+1] = min(dp[i][j+1],dp[i][j])
        else:
            dp[i+1][j]  = min(dp[i+1][j] ,dp[i][j])
            dp[i][j+1] = min(dp[i][j+1],dp[i][j])

            
        
ans = dp[h-1][w-1]
if s[0][0] == '#':ans += 1
print(ans)