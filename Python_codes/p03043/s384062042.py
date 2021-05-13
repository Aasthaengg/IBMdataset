import math
from decimal import Decimal
N, K = map(int, input().split())

ans = 0
for i in range(N):
  tmp = i+1
  count = 0
  while tmp < K:
    tmp *= 2
    count += 1
  ans += 1/(2**count)
ans *= (1/N)
print(ans)
