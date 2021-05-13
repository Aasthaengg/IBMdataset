n,m = map(int,input().split())

a = [0] * (n+1)
dp = [0] * (n+1)
mod = 1000000007

for i in range(m):
	num = int(input())
	a[num] = 1

dp[0]=1

for i in range(1,n+1):
	if a[i] == 1:
		continue

	dp[i] += dp[i-1]
	if i>1:
		dp[i] += dp[i-2]

	dp[i] = dp[i] % mod

print(dp[n]%mod)