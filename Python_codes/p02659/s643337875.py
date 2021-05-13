import math
from decimal import Decimal
A, B = map(str, input().split())
ans = int(math.floor(int(A) * Decimal(B)))
print(ans)
