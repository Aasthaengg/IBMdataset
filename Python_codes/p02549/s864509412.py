n, k = map(int, input().split())
sec = [list(map(int, input().split())) for _ in range(k)]
sec.sort()
    
mod = 998244353
    
dp = [0] * n
dp[0] = 1
sum_dp = [0, 1]
for i in range(1, n):
    for l, r in sec:
        if i - l < 0:
            break
        elif i - r > 0:
            dp[i] = ((dp[i] + sum_dp[i-l+1]) % mod - sum_dp[i-r]) % mod
        else:
            dp[i] = (dp[i] + sum_dp[i-l+1]) % mod
    
    sum_dp.append((sum_dp[-1] + dp[i]) % mod)
    
print(dp[n-1])
