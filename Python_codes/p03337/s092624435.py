def resolve():
	a, b = map(int, input().split())
	v = max(a+b, a-b, a*b)
	print(v)
resolve()