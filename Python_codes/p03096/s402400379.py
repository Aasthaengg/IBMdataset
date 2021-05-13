n, *cs = map(int, open(0))
fwd = [0] * n
mod = 10 ** 9 + 7
d = {}
for i, c in enumerate(cs[::-1], start=1):
	f = d.get(c, 0)
	if f:
		fwd[n - i] = f
	d[c] = n - i
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
	dp[i] += dp[i - 1]
	dp[i] %= mod
	# 隣だったら無視
	if fwd[i - 1] > i:
		dp[fwd[i - 1] + 1] += dp[i]
print(dp[-1])