import math

X = int(input())

for x in range(X, 2 * X + 1):
	for i in range(2, int(math.sqrt(x)) + 1):
		if x % i == 0:
			break
	else:
		print(x)
		break