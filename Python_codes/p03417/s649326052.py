def flip(x):
	if x:
		return False
	else:
		return True


n, m = [int(el) for el in input().split(' ')]

if n > 1 and m > 1:
	print((n-2)*(m-2))
elif n == 1 and m > 1:
	print(m-2)
elif n > 1 and m == 1:
	print(n-2)
else:
	print(1)