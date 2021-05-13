n, k = map(int, input().split())
ls = list(map(int, input().split()))
dp = [False] * (k + 1)
for i in range(1, k + 1):
	for j in ls:
		if i - j >= 0 and not dp[i - j]:
			dp[i] = True
if dp[k]:
	print('First')
else:
	print('Second')
