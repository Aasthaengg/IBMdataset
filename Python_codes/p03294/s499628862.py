import math
from functools import reduce

def lcm_base(x,y):
	return (x*y)//math.gcd(x,y)

def lcm_list(numbers):
	return reduce(lcm_base, numbers, 1)

n=int(input())
a=list(map(int,input().split()))
b=0
c=lcm_list(a)-1

for A in a:
	b+=c%A

print(b)