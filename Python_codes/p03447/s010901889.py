def resolve():
	x, a, b = [int(input()) for _ in range(3)]
	v = (x - a) % b
	if v:
		print(v)
	else:
		print(0)
resolve()