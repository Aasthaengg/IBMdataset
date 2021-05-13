from math import gcd
n=int(input())
a=int(input())

for i in range(n-1):
    b=int(input())
    g=gcd(a,b)
    a=a*b//g

print(a)