import math

def isPrime(x):
	if x == 2:
		return True

	if x < 2 or x % 2 == 0:
		return False

	i = 3
	while i <= math.sqrt(x):
		if x % i == 0:
			return False
		i = i + 2

	return True

if __name__ == '__main__':
	n = int(input())
	A = [int(input()) for i in range(n)]

	cnt = 0
	for i in range(n):
		if isPrime(A[i]) == True:
			cnt = cnt + 1

	print(cnt)