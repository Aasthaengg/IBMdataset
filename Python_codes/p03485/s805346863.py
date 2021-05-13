import math

def resolve():
	n = list(map(int, input().split()))
	print(math.ceil(sum(n)/2))
resolve()