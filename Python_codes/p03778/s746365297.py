def resolve():
	w, a, b = map(int, input().split())
	if a + w < b or b + w < a:
		print(min(abs(a+w - b), abs(b+w - a)))
	else:
		print(0)
resolve()