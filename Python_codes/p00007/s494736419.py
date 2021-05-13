import math

debt = 100
n = int(input())

for _ in range(n):
	debt = math.ceil(debt * 1.05)

print(debt * 1000)