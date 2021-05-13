import math
n = input()
prime_count = 0
is_prime = 1

for i in range(0,n):
	is_prime = 1
	prime_check_number = input()
	if prime_check_number == 2:
		prime_count = prime_count + 1
		continue
	elif prime_check_number == 1 or prime_check_number % 2 == 0:
		continue
	else:
		prime_check_number_sqrt = int(math.sqrt(prime_check_number))
		for j in range(3,prime_check_number_sqrt+1,2):
			if prime_check_number % j == 0:
				is_prime = 0
				break

	if is_prime == 1:
		prime_count = prime_count + 1

print(prime_count)
