import math
from decimal import Decimal
n, m, d = map(int, input().split())
if d == 0:
    t = math.exp(float(Decimal.from_float(math.log(n)+math.log(m-1)-2*math.log(n))))
    print(t)
else:
    t = 2.0 * (n - d)*(m-1) / n ** 2
    print(t)