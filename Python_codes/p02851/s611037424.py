from itertools import accumulate
from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
A_cum = [0] + list(accumulate(A))

ans = 0
dd = defaultdict(int)
q = []
for i, a in enumerate(A_cum):
  a -= i
  a %= K
  if i-K >= 0:
    dd[q[i-K]] -= 1
  ans += dd[a]
  dd[a] += 1
  q.append(a)
print(ans)  
