import math
X = int(input())
gcd = math.gcd(X, 360)
lcm = X * 360 / gcd
print(int(lcm/X))