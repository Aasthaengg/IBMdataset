def resolve():
	a, b = input().split()
	c = {
		'D': -1,
		'H': 1,
	}
	ans = c[a] * c[b]
	if ans > -1:
		print("H")
	else:
		print("D")
resolve()