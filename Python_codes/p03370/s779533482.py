def resolve():
	n, x = map(int, input().split())
	m = [int(input()) for _ in range(n)]
	x -= sum(m)
	v = n + (x//min(m))
	print(v)
resolve()