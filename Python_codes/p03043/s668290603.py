import math
from fractions import Fraction
N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
  if i >= K:
    ans += Fraction(1, N)
  else:
    ans += Fraction(1, N) * Fraction(1, 2) ** (math.ceil(math.log2(K / i)))
  
print(float(ans))