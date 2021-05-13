n, t = map(int, input().split())
A = list(map(int, input().split()))
from collections import defaultdict
prof = defaultdict(int)
low = 10**9
for a in A:
  if a > low: prof[a - low] += 1
  else: low = a
kmax = max(prof.keys())
ans = prof[kmax]
print(ans)