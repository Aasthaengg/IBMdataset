n= int(input())
a=int(input())

import math
if n==1:
	print(a)
	exit()

b=int(input())
c=(a*b)//math.gcd(a,b)
for i in range(n-2):
	b=int(input())
	c=(c*b)//math.gcd(c,b)

print(c)