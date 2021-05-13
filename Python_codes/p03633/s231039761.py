import math

def calc_lcm(x, y):
    return (x * y) // math.gcd(x, y)

N,*T = map(int,open(0).read().split())

lcm = 1

for i in T:
  lcm = calc_lcm(lcm,i)
print(lcm)