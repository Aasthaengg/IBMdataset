import math
a,b,c,d=map(int,input().split())
mc = b//c-(a-1)//c
md = b//d-(a-1)//d
cd = (c*d)//math.gcd(c,d)
mcd = b//cd - (a-1)//cd

print(b-a+1 - mc-md+mcd)
