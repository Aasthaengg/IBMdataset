X = int(input())
ans = 0
import math
while True:
	for x in range(2, int(math.sqrt(X)) + 1):
		if X % x == 0:
			break
	else:
		print(X)
		break
	X += 1
