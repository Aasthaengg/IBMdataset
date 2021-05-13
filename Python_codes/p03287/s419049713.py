n, m = map(int, input().split())
l = list(map(int, input().split()))

l = [0] + l
from itertools import accumulate
cum =list(accumulate(l))
cum = [c%m for c in cum]

d = {}
ans = 0
for i in range(n+1):
  if cum[i] not in d:
    d[cum[i]] = 1
  else:
    ans += d[cum[i]]
    d[cum[i]] += 1
print(ans)