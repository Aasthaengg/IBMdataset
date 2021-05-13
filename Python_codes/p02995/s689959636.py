import math

A,B,C,D = map(int, input().split())

a = A - 1
bn = B - B//C - B//D + (B//((C*D)//math.gcd(C,D)))
an = a - a//C - a//D + (a//((C*D)//math.gcd(C,D)))
print(bn - an)