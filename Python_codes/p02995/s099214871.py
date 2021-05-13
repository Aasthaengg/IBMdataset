def gcd(a,b):
	return max(a,b) if min(a,b)==0 else gcd(min(a,b),max(a,b)%min(a,b))
a,b,c,d=map(int,input().split())
l=c*d//gcd(c,d)
cc=b//c-(a-1)//c
dd=b//d-(a-1)//d
ll=b//l-(a-1)//l
print(b-a+1-(cc+dd-ll))