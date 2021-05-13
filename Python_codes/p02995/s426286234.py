import math
a,b,c,d = map(int,input().split()) 

def lcm(x, y):
    return (x * y) // math.gcd(x, y)
a-=1
e=lcm(c,d)

ansb=0
ansb += b//c
ansb += b//d
ansb -= b//e



ansa=0
ansa += a//c
ansa += a//d
ansa -= a//e
print((b-a)-(ansb-ansa))