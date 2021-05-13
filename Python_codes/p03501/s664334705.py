def resolve():
	n, a, b = map(int, input().split())
	print(min(a*n, b))
resolve()