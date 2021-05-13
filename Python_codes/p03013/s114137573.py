n,m = map(int,input().split())

a = [0] * (n+2)
dp = [0] * (n+2)
mod = 1000000007

for i in range(m):
	num = int(input())
	a[num] = 1

dp[0]=1

for i in range(0,n):
	if a[i] == 1:
		continue
	dp[i] = dp[i]%mod
	dp[i+1] += dp[i]
	dp[i+2] += dp[i]

print(dp[n]%mod)