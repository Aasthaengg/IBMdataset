from math import gcd
N = int(input())
ans = 1
for i in range(N):
  n = int(input())
  ans = ans * n // gcd(ans, n)
print(ans)