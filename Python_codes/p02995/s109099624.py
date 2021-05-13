import math

a,b,c,d=map(int,input().split())

x=(a-1)//c

y=b//c
z=(a-1)//d
w=b//d

e=(c * d) // math.gcd(c, d)

p=(a-1)//e

q=b//e

print(b-a+1-y+x-w+z+q-p)
