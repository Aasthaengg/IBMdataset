import math
X = int(input())
lcm = 360 * X // math.gcd(360, X)
print(lcm // X)