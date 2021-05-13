import math
def taxr(n):
	x = math.ceil(n / 1.08)
	if int(x * 1.08) == n:
		return x
	else:
		return ':('
n = int(input())
print(taxr(n))