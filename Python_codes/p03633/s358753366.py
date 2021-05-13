import math
N = int(input())
P = [int(input()) for _ in range(N)]

a = 1
for p in P:
  g = math.gcd(a,p)
  a = a * p // g

print(a)