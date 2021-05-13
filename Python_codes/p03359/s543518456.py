def resolve():
	a, b = map(int, input().split())
	v = 0
	if a <= b:
		print(a)
	else:
		print(a-1)

resolve()