import math
while True:
	try:
		a, b = map(int, input().split())
		print(int(math.gcd(a,b)),(a*b) // int(math.gcd(a,b)))
	except:
		break
