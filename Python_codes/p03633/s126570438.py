def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a % b)
def lcm(a,b):
	return a * b / gcd(a,b)
print reduce(lcm, [int(raw_input()) for oo in range(int(raw_input()))])