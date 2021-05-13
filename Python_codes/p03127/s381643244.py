from math import gcd
N = int(input())
A = list(map(int, input().split()))
for i, a in enumerate(A):
  if i == 0:
    g = a
    continue
  g = gcd(g, a)
print(g)