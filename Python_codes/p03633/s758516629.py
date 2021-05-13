def gcd(a, b):
	if a == 0:
		return b
	return gcd(b % a, a)
n = int(input())
res = int(input())
while n > 1:
	x = int(input())
	res = (res * x) // gcd(res, x);
	n -= 1
print(res)