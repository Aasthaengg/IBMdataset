h,w=map(int,input().split())

a = [input() for _ in range(h)]
dp=[[0 for i in range(w)] for j in range(h)]
MOD=10**9+7
if a[0][0]==".":
    dp[0][0]=1

for i in range(h):
    for j in range(w):
        if a[i][j]==".":
            if j-1>=0 :
                dp[i][j]+=dp[i][j-1]
            if i-1>=0:
                dp[i][j]+=dp[i-1][j]
            dp[i][j]%=MOD
        else:
            continue

print(dp[h-1][w-1]%MOD)