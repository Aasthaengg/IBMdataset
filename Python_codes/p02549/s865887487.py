# DP, 累積和
n, k = list(map(int, input().split()))
s = list()
for i in range(k):
     l, r = list(map(int, input().split()))
     s.append((l, r))

mod = 998244353
i = 1
dp = [0] * (n+1)
dp[1] = 1
dpsum = [0] * (n+1)
dpsum[1] = 1
for i in range(2, n+1):
    for l, r in s:
        li = i-r
        ri = i-l
        if ri < 1: continue
        li = max(li, 1)
        dp[i] = (dp[i] + dpsum[ri] - dpsum[li-1]) % mod
    dpsum[i] = (dpsum[i-1] + dp[i]) % mod
    
print(dp[n])
