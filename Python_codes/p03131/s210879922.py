k, a, b = map(int, input().split())

if b <= a + 1:
	print(k + 1)
else:
	n = (k - (a - 1)) // 2
	r = (k - (a - 1)) % 2
	if r == 0:
		print(n * b - (n - 1) * a)
	elif r == 1:
		print(n * b - (n - 1) * a + 1)