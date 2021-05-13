import math

def is_prime(num):
	prime = True
	for i in range(2,int(math.sqrt(num))+1):
		if num%i == 0:
			prime = False
			break
	return prime

num_set = set()
try:
	while True:
		num_set.add(eval(input()))
except EOFError:
	count = 0
	for x in num_set:
		count = count + (1 if is_prime(x) else 0)
	print(count)