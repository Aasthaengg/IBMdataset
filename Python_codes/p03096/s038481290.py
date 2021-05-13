n = int(raw_input())
s = [int(raw_input()) for _ in range(n)]
mod = int(1e9+7)

previous_idx = {}
dp = [1] * n
ans = 1

for i in range(n):
	c = s[i]
	if c in previous_idx and previous_idx[c] != i-1:
		ans += dp[previous_idx[c]]

	previous_idx[c] = i
	dp[i] = ans % mod

print(ans % mod)
