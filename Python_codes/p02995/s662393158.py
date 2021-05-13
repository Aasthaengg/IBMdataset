import math
def lcm(x, y):return (x * y) // math.gcd(x, y)
a,b,c,d=map(int,input().split())

e = lcm(c,d)
print(b-a+1-(b//c-(a-1)//c)-(b//d-(a-1)//d)+(b//e-(a-1)//e))