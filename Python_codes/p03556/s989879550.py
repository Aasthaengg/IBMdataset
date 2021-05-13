import math

def resolve():
	n = int(input())
	for i in range(n, -1, -1):
		sr = math.sqrt(i)
		if sr - math.floor(sr) == 0:
			print(i)
			return
resolve()