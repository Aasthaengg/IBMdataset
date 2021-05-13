def resolve():
	a, b = map(int, input().split())
	ans = a + b if 24 - (a + b) > 0 else (a + b) - 24
	print(ans)
resolve()