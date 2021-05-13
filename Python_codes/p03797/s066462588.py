def resolve():
	n, m = map(int, input().split())
	if m <= n:
		print(m // 2)
	else:
		t = m - (n*2)
		print(n + t//4)
resolve()