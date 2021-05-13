import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
n = int(readline())
a = list(map(int, readline().split()))
b = defaultdict(list)
c = defaultdict(list)

for i, v in enumerate(a, 1):
  b[i + v].append(i)
  if 2 <= i - v <= 100000001:
    c[i - v].append(i)
c = dict(c)

ans = 0
for v, L in b.items():
  for j in L:
    if v in c:
      ans += len(c[v])
print(ans)