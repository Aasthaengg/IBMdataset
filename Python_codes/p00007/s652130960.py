import sys
import math as m
n=int(input())
out=100000
for i in range(n):
	out=m.ceil(out*1.05/1000)*1000
print(out)

#for i in sys.stdin:
#	a,b=map(int,i.split())
#	print(gcd(a,b),lcm(a,b))