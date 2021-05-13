N = int(input())

def check_divisor(number):
	divisors = 0
	for j in range(1, number+1, 2):
		if not (number%j):
			divisors += 1
			if divisors == 9: return False
	if divisors == 8: return True
	else: return False

count = 0
for i in range(1, N+1, 2):
	if check_divisor(i):
		count += 1
print(count)