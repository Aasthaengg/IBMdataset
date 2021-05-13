import math


def isPrime(n):
	if n == 2:
		return True

	if n < 2 or n % 2 == 0:
		return False

	i = 3
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 2

	return True


num = int(input())
numbers = [int(input()) for i in range(num)]

count = 0
for i in range(num):
    if isPrime(numbers[i]) == True:
        count += 1
print(count)