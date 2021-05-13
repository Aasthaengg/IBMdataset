def main():
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
	for i, fwd in enumerate(fwd, start=1):
		dp[i] += dp[i - 1] % mod
		if fwd > i:
			dp[fwd + 1] += dp[i] % mod
	print(dp[-1] % mod)

if __name__=="__main__":
	main()