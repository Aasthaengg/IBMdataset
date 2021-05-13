def resolve():
	n, x = map(int, input().split())
	a = list(map(int, input().split()))
	c = 0
	for i in range(n-1):
		if a[i] + a[i+1] > x:
			st = (a[i] + a[i + 1]) - x
			a[i+1] = a[i+1] - st if a[i+1] > st else 0
			c += st
	print(c)
resolve()