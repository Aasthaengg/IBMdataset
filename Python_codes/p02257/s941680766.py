#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C

import math

num = int(input())

result = 0

while num > 0:
	x = int(input())
	isPrime = 0
	if x == 2:
		isPrime = 1
	elif x < 2 or x % 2 == 0:
		pass
	else:
		i = 3
		isPrime2 = 1
		while i <= math.sqrt(x):
			if x % i == 0:
				isPrime2 = 0
				break
			i = i + 2
		if isPrime2:
			isPrime = 1
	if isPrime:
		result += 1
	num -= 1

print(result)