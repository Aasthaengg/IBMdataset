def resolve():
	n, k = map(int, input().split())
	x = list(map(int, input().split()))
	ans = float('inf')
	for i in range(n-(k-1)):
		if abs(x[i] - x[i+(k-1)]) == (abs(x[i]) + abs(x[i+(k-1)])):
			v = abs(x[i] - x[i + (k - 1)]) + min(abs(x[i]), abs(x[i + (k - 1)]))
			ans = min(ans, v)
		else:
			v = max(abs(x[i]), abs(x[i + (k - 1)]))
			ans = min(ans, v)
	print(ans)
resolve()