import math
N = int(input())
lcm = int(input()) #T0
for i in range(N-1):
    x = int(input())
    lcm = lcm * x // math.gcd(lcm,x)
print(lcm)