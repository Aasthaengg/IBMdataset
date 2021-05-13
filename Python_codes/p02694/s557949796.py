import math
from decimal import Decimal

X = int(input())

m = 100
c = 1

while True:
    m_ = m + math.floor(m*Decimal("0.01"))
    if m_ >= X:
        print(c)
        break
    c += 1
    m = m_