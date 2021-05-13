H,W=map(int, input().split())
a= ["#"*(W+1)] + ["#" + input() for _ in range(H)]
dp=[[0]*(W+1) for _ in range(H+1)]
MOD=10**9+7
dp[1][1] = 1
for i in range(1, H+1):
    for j in range(1, W+1):
        if i == 1 and j == 1:
            continue
        if a[i][j] == ".":
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD
print(dp[H][W]%MOD)