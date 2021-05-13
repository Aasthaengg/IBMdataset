import numpy as np

x,k,d = map(int, input().split())

x = np.abs(x)

if x - k * d > 0:
	print(x - k * d)
elif x == d:
	if k % 2 == 0: print(x)
	else:print(0)
else:
	times = k - x // d
	num1 = x % d
	num2 = num1 - d
	if times % 2 == 0:
		print(np.abs(num1))
	else:
		print(np.abs(num2))
