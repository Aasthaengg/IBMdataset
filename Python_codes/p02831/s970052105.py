def gcd(a,b):
	return gcd(b, a% b) if b else a
a,b = map(int,raw_input().split(' '))
print a * b / gcd(a,b)