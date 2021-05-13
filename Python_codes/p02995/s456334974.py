import math
a,b,c,d=map(int,input().split())
a-=1
h=int(c*d/math.gcd(c,d))
e=b//c-a//c
f=b//d-a//d
g=b//h-a//h
print(b-a-e-f+g)