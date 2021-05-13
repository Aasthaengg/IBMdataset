n,m = map(int,input().split())

a = []
dp = []
mod = 1000000007

for i in range(100100):
	a.append(0)
	dp.append(0)

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