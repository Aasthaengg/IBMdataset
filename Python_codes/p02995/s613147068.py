import math
a,b,c,d = map(int,input().split())
g = c*d//math.gcd(c,d)
print(b-a+1-((b//c-(a-1)//c)+(b//d-(a-1)//d)-(b//g-(a-1)//g)))