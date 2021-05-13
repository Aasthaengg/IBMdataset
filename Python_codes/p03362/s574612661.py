n = int(input())

import math
def is_prime(n):
	if n == 1:
		return False
	
	for k in range(2, int(math.sqrt(n)) + 1):
		if n%k == 0:
			return False
	return True
s = []
for i in range(1,10**6):
	if is_prime(i):
		if i%5 == 1:
			s.append(i)
	if len(s) == n:
		break
print (*s)
