n, a, b = map(int, input().split())

if (b - a) % 2 == 0:
	print((b - a) // 2)
elif (b - a) % 2 == 1:
	na = n - a
	nb = n - b
	a1 = a - 1
	b1 = b - 1
	if na + nb <= a1 + b1:
		print((na + nb + 1) // 2)
	else:
		print((a1 + b1 + 1) // 2)