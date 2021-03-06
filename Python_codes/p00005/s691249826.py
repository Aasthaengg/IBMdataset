import sys;

def gcd(a, b):
	if b == 0:
		return a;
	return gcd(b, a % b);
	
def lcm(a, b):
	return a * b // gcd(a, b);

for line in sys.stdin:
	[a, b] = [int(num) for num in line.split()];
	print(str(gcd(a, b)) + ' ' + str(lcm(a, b)));