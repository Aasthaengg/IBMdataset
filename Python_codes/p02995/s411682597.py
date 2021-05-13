from fractions import gcd

a,b,c,d=map(int,input().split())

nc=b//c-(a-1)//c
nd=b//d-(a-1)//d
cd=c*d//gcd(c,d)
ncd=b//cd-(a-1)//cd

print(b-a+1-nc-nd+ncd)