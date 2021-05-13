import math
a,b,c,d = map(int,input().split())
lcm = c*d//(math.gcd(c,d))
e,f,g = b//c - (a-1)//c,b//d - (a-1)//d,b//(lcm) - (a-1)//(lcm)
print(b-a+1-e-f+g)