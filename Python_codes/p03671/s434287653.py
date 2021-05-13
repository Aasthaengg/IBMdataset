def resolve():
	n = list(map(int, input().split()))
	m = max(n)
	print(sum(n) - max(n))
resolve()