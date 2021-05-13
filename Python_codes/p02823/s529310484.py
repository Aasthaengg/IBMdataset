n, a, b = map(int, input().split())
if (a - b) % 2 == 0:
	print(abs(a - b) // 2)
else:
	if a - 1 < n - b:
		print(((a - 1) + (b - 1)) // 2 + 1)
	else:
		print(((n - a) + (n - b)) // 2 + 1)