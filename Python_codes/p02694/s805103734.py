X = int(input())
x = 100
y = 0
import math
while True:
	x = math.floor(x + (x // 100))
	y += 1
	if x >= X:
		print(y)
		break
