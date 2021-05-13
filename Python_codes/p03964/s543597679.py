from decimal import Decimal
from math import ceil

n = int(input())
ratio = [list(map(int, input().split())) for _ in range(n)]

t_voted = a_voted = 1
for t, a in ratio:
    val = max(ceil(Decimal(t_voted) / Decimal(t)), ceil(Decimal(a_voted) / Decimal(a)))
    t_voted = t * val
    a_voted = a * val

print(t_voted + a_voted)
