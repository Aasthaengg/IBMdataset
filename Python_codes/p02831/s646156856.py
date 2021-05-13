from math import *
n,m=map(int,input().split())
g=gcd(n,m)
print((n*m)//g)
