from math import gcd
X, Y = [int(i) for i in input().split()]
lcm = X * Y // gcd(X, Y)
if lcm == X:
    print(-1)
else:
    print(X)
