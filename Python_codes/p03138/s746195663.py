n, k, *a = map(int, open(0).read().split())
l = k.bit_length()
pre = sum((x >> l) << l for x in a)
dp = [[0] * 2 for _ in range(l + 1)]
dp[0] = [pre, -float("inf")]
for i in range(l):
	t = 1 << l - i - 1
	s = sum(x & t for x in a)
	ms = t * n - s
	if k & t:
		dp[i + 1][0] = dp[i][0] + ms
		dp[i + 1][1] = max(dp[i][1] + max(s, ms), dp[i][0] + s)
	else:
		dp[i + 1][0] = dp[i][0] + s
		dp[i + 1][1] = dp[i][1] + max(s, ms)
print(max(dp[-1]))