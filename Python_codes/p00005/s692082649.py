def GcdLcm(a, b):
	p = a * b
	if a < b:
		a, b = b, a
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return [b, int(p / b)]

while True:
	try:
		a, b = [eval(item) for item in input().split()]
		g, l = GcdLcm(a, b)
		print(str(g), str(l))
	except EOFError:
		break