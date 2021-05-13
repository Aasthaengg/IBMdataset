import math
a,b,c,d=list(map(int,input().split()))
a-=1
def calculation(x,c,d):
	x=x-(x//c)-(x//d)+(x//((c*d)//math.gcd(c,d)))
	return x
	
print(calculation(b,c,d)-calculation(a,c,d))