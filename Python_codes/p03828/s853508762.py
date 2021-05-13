import math
n = int(input())
mod = 10**9+7

def is_prime(n):
	if n == 1:
		return False
	
	for k in range(2, int(math.sqrt(n)) + 1):
		if n%k == 0:
			return False
	return True

p = []
for i in range(1,n+1):
	if is_prime(i):
		p.append(i)
ans = 1
for i in p:
	s = 0
	x = i
	while x <= n:
		s += n//x
		x *= i
	ans *= (s+1)
	ans %= mod
print (ans)
