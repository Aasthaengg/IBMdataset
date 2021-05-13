import math

A, B = (int(x) for x in input().split())

def lcm(x, y):
  return (x*y) // math.gcd(x, y)

print(lcm(A, B))