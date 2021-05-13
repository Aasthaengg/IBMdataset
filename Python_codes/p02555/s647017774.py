import sys; input = sys.stdin.readline

s = int(input())
mod = int(1e9)+7
dp = [0]*(s+1)
dp[0] = 1
for i in range(3, s+1):
	for j in range(3, s+1):
		if i>=j: dp[i] = (dp[i] + dp[i-j])%mod
print(dp[s])