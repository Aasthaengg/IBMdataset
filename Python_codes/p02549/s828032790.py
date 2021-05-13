n, k = map(int, input().split())

l = [0] * k
r = [0] * k
dp = [0] * (n+1)
dpsum = [0] * (n+1)
dp[1] = 1
dpsum[1] = 1

for i in range(k):
    l[i], r[i] = map(int, input().split())

for i in range(2, n+1):
    for j in range(k):
        li = max(1, i - r[j])
        ri = i - l[j]
        if ri >= 0:
            dp[i] += dpsum[ri] - dpsum[li-1]
    dp[i] = dp[i] % 998244353
    dpsum[i] = (dpsum[i-1] + dp[i]) % 998244353
    
print(dp[n])
