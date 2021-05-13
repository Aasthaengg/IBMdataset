n, k = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(k)]
dp = [0 for i in range(n+1)]
mod = 998244353
lr.sort()
a = [0]*(n+1)
dp[0]=1; a[0]=1
for i in range(1,n+1):
    for l, r in lr:
        if i-l<0: continue
        elif i-l>=0 and i-r-1<0: dp[i]+=a[i-l]
        else: dp[i]+=a[i-l]-a[i-r-1]
    dp[i]%=mod
    a[i]=a[i-1]+dp[i]
    a[i]%=mod
print(dp[n-1]%mod)