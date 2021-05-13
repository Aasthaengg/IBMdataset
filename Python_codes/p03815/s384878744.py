def resolve():
	x = int(input())
	r = 0
	if x % 11 > 6:
		r = 2
	elif x % 11:
		r = 1

	print((x // 11 * 2) + r)
resolve()