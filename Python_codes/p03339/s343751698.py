def resolve():
	n = int(input())
	s = input()
	west_sum = [0]*(n+1)
	east_sum = [0]*(n+1)

	for i in range(n):
		if s[i] == 'E':
			east_sum[i+1] = east_sum[i] + 1
			west_sum[i+1] = west_sum[i]
		else:
			west_sum[i+1] = west_sum[i] + 1
			east_sum[i+1] = east_sum[i]
	ans = float('inf')
	for i in range(1, n):
		if i == 1:
			ans = min(ans, east_sum[-1] - east_sum[1])
		elif i == (n - 1):
			ans = min(ans, west_sum[-2])
		else:
			v = west_sum[i-1] + (east_sum[-1] - east_sum[i])
			ans = min(ans, v)
	print(ans)
resolve()