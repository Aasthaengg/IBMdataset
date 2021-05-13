import math

n=int(input())
a=int(n*360/math.gcd(n,360))
if n==360:
    print(1)
else:
    print(int(a/n))