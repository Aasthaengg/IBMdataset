n,k = map(int,input().split())
mod = 998244353

l,r = [0]*k,[0]*k
for i in range(k):
    ll,rr = map(int,input().split())
    l[i],r[i] = ll,rr

dp = [0]*(n+1)
dpsum = [0]*(n+1)
dp[1], dpsum[1] = 1,1
for i in range(2,n+1):
    for j in range(k):
        li = i - r[j]
        ri = i - l[j]
        if ri < 0:
            continue
        dp[i] += dpsum[ri] - dpsum[li-1]
        dp[i] %= mod
    dpsum[i] = dpsum[i-1] + dp[i]
print(dp[n])