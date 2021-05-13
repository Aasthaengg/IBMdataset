N, K = map(int, input().split())
MOD = 998244353

l = [0] * K
r = [0] * K

for i in range(K):
	l[i], r[i] = map(int, input().split())
	
dp = [0] * (N+1)
dp[1] = 1

dpsum = [0] * (N+1)
dpsum[1] = 1

for i in range(2, N+1):
	for j in range(K):
		li = i - r[j]
		ri = i - l[j]
		if li <= 0:
			dp[i] = dp[i] + dpsum[ri]
			dp[i] %= MOD
		else:
			dp[i] = dpsum[ri] - dpsum[li-1] + dp[i]
			dp[i] %= MOD
			
			
	dpsum[i] = dp[i] + dpsum[i-1]
	dpsum[i] %= MOD
	
print(dp[N] % MOD)