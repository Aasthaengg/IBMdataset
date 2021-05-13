import math
from decimal import Decimal
a, b, x = list(map(int, input().split()))

print(math.floor(Decimal(b)/x) - math.ceil(Decimal(a)/x) + 1)