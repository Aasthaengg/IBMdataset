import math
def lcm(x,y):
    return(x*y)//math.gcd(x,y)

a,b,c,d=map(int,input().split())
e=b//c-(a-1)//c
f=b//d-(a-1)//d

g=b//lcm(c,d)-(a-1)//lcm(c,d)
ans=e+f-g
#print(e,f,g)
print(b-a+1-ans)

