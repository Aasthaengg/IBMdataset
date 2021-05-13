import math
import statistics
from decimal import Decimal, ROUND_HALF_UP
a = int(input())
b = list(map(int, input().split()))
c = statistics.mean(b)
d = Decimal(c).quantize(Decimal('1'), ROUND_HALF_UP)
ans = 0
for i in range(a):
  ans += (d - b[i])**2
print(ans)
