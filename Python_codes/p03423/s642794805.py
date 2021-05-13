n = int(input())

a, b = divmod(n, 3)
if n < 3:
	print(0)
else:
	print(a)