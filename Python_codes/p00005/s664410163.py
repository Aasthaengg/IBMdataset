def get_gcd(a,b):
	if a > b: a, b = b, a
	if b % a == 0:
		return a
	else:
		return get_gcd(a, b % a)

def get_lcm(a,b,g):
	return a * b / g

while True:
	try:
		a,b = map(int, sorted(raw_input().split()))
		GCD = get_gcd(a,b)
		LCM = get_lcm(a,b,GCD)
		print "{} {}".format(GCD, LCM)
	except EOFError:
		break