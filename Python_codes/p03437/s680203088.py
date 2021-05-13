from math import gcd
X, Y = map(int, input().split())
l = X * Y // gcd(X, Y)
if l == X:
    print(-1)
else:
    print(X)
