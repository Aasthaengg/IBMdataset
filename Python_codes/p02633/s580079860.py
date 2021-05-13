from math import gcd
x = int(input())

lcm = (x * 360)/gcd(x, 360)
print(int(lcm/x))
