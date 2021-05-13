from decimal import Decimal
N = int(input())
A = list(map(Decimal, input().split()))

ans = 0
for a in A:
  ans += Decimal(1) / a
print(float(Decimal(1) / ans))