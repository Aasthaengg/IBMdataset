def resolve():
	n, m = map(int, input().split())
	v = 2**m*(m*1900 + (n-m)*100)
	print(v)
resolve()