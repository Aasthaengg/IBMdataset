def resolve():
	t = []
	for _ in range(3):
		t.append(int(input()))
	a, b, h = t
	print(int((a+b)/2*h))
resolve()