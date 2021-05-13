import math
N=int(input())
g=int(input())
for _ in range(N-1):
  T=int(input())
  g=g*T//math.gcd(g,T)
print(g)