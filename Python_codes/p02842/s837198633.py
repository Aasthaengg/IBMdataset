import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

import decimal
import math
N = ri()
for i in range(N + 1):
    if math.floor(i * decimal.Decimal(1.08)) == N:
        print(i)
        exit()
print(':(')