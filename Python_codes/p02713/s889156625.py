from math import gcd

k = int(input())
ans = 0

for i in range(1, k + 1):
  for j in range(1, k + 1):
    ij = gcd(i, j)
    for t in range(1, k + 1):
      ans += gcd(ij, t)

print(ans)
