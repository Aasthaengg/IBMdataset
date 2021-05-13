import math
from decimal import Decimal
X = int(input())
now = 100
year = 0

while True:
    if now >= X:
        break
    now = int(now * Decimal("1.01"))
    year += 1

print(year)
