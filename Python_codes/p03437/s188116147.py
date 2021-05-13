from fractions import gcd
X, Y = map(int, input().split())
if (gcd(X, Y) == Y):
    print(-1)
else:
    print(X)
