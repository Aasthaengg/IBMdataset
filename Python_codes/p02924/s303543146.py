from decimal import *

n = int(input())
nn = Decimal(n)
ans = nn * (nn - 1) / 2
#ans = n * (n - 1) / 2
print(int(ans))
