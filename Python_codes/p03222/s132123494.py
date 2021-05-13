mod = 10**9+7
H,W,K = map(int,input().split())
a = [0]*20
a[0]=1
a[1]=1
for i in range(10):
    a[i+2]=a[i+1]+a[i]
dp = [[0]*(W+1) for _ in range(H+1)]
dp[0][0] = 1
for h in range(H):
    for k in range(W):
        dp[h+1][k] += a[k]*a[W-k-1]*dp[h][k]
        dp[h+1][k] += a[k-1]*a[W-k-1]*dp[h][k-1]
        dp[h+1][k] += a[k]*a[W-k-2]*dp[h][k+1]
        dp[h+1][k] %= mod
print(dp[H][K-1])