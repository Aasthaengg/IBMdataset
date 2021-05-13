from decimal import Decimal
from fractions import Fraction
n, k = map(int, input().split())

prob = []

for base in range(1, n+1):
  p = 0
  while (base < k):
    p += 1
    base = base * 2
  prob.append(Fraction(1, n * (2 ** p)))
print(Decimal(sum(prob).numerator / sum(prob).denominator))
