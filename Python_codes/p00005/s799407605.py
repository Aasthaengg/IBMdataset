def gcd(a,b):
	a,b=max(a,b),min(a,b)	
	while b!=0:
		a,b=b,a%b
	return a

def lcm(a,b):
	return a*b//gcd(a,b)


while True:
	try:
		x,y=map(int,input().split())
		print(gcd(x,y),lcm(x,y))

	except EOFError:
		break