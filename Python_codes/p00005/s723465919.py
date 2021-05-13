import sys

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def lcm(a, b):
	return a * b // gcd (a, b)

for line in sys.stdin:
	a, b = map(int , line.split())
	print gcd(a,b), lcm(a,b)