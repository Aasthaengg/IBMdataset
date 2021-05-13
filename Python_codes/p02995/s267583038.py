import fractions

a,b,c,d=map(int,open(0).read().split())

e=c*d//fractions.gcd(c,d)

nc=b//c-(a-1)//c
nd=b//d-(a-1)//d
ne=b//e-(a-1)//e

print(b-a+1-nc-nd+ne)