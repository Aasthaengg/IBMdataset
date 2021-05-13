s=input()
n=len(s)
mod=10**9+7
dp=[[0]*13 for _ in range(n+1)]
dp[0][0]=1
mul=1

for i in range(n):
    x=s[-(i+1)]  # 後ろから見ていく
    if x=='?':
        for k in range(10):
            for j in range(13):
                dp[i+1][(mul*k+j)%13]+=dp[i][j]
                dp[i+1][(mul*k+j)%13]%=mod
    else:
        k=int(x)
        for j in range(13):
            dp[i+1][(mul*k+j)%13]+=dp[i][j]
            dp[i+1][(mul*k+j)%13]%=mod
    mul=mul*10%13
# print(dp)
print(dp[n][5])
