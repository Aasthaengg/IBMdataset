MOD = 10 ** 9 + 7
N = int(input())
from collections import Counter
c = Counter(input())

x = 1
for v in c.values():
  x *= (v + 1)

ans = x - 1
print(ans%MOD)