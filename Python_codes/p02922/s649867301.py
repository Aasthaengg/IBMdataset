import math
def powerSocket(a, b):
	return math.ceil((b-1)/(a-1))
a, b = map(int, input().split())
print(powerSocket(a, b))