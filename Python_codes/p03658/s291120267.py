def resolve():
	n, k = map(int, input().split())
	l = sorted(list(map(int, input().split())))
	print(sum(l[n-k:]))
resolve()