import sys

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

def lcm(a,b):
	return a*b/gcd(a,b)

for s in sys.stdin:
	i = map(int,s.split())
	print gcd(*i), lcm(*i)