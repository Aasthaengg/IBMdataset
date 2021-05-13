from math import gcd
a,b,c,d = map(int, input().split())

s = b - ((b//c)+(b//d)) + b//((c*d)//gcd(c,d))
t = (a-1) - (((a-1)//c)+((a-1)//d)) + (a-1)//((c*d)//gcd(c,d))
print(s-t)