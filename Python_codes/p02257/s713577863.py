import math

def isprime(x):
	sq = int(math.sqrt(x))
	for i in range(2, sq + 1):
		if x % i == 0:
			return False
	return x != 1

array = []
N = int(raw_input())
for i in range(0, N):
	array.append(int(raw_input()))

count = 0
for i in array:
	if isprime(i):
		count += 1
print count