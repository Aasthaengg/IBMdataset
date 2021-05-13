h,w,K=map(int,input().split())
mod=10**9+7
dp=[[0]*(w+1) for _ in range(h+1)]
dp[0][0]=1
for i in range(h):
    for j in range(w):
        for k in range(2**(w-1)):
            ok=True
            for l in range(w-2):
                if (k>>l)&1 and (k>>(l+1))&1:
                    ok=False
            if ok:
                if j>=1 and (k>>(j-1))&1:
                    dp[i+1][j-1]+=dp[i][j]
                    dp[i+1][j-1]%=mod
                elif j<=w-2 and (k>>j)&1:
                    dp[i+1][j+1]+=dp[i][j]
                    dp[i+1][j+1]%=mod
                else:
                    dp[i+1][j]+=dp[i][j]
                    dp[i+1][j]%=mod

print(dp[h][K-1])
