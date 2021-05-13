from math import gcd
X = int(input())
lcm = X * 360 // gcd(X, 360)
print(lcm//X)