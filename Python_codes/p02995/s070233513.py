import math

A, B, C, D = map(int,input().split())
lcm = C*D//math.gcd(C,D)

c = B//C - (A-1)//C
d = B//D - (A-1)//D
cd = B//lcm - (A-1)//lcm

print(B-A+1 - c - d + cd)