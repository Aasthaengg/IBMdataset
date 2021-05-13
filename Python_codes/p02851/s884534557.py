from itertools import accumulate
from collections import defaultdict
N, K = map(int, input().split())
A = [0] + [a-1 for a in map(int, input().split())]
A_cum = list(accumulate(A))
A_cum = [a%K for a in A_cum]

ans = 0
dd = defaultdict(int)
q = []
for j in range(N+1):  
  ans += dd[A_cum[j]]
  dd[A_cum[j]] += 1
  q.append(A_cum[j])
  if len(q) == K:
    dd[q[0]] -= 1
    q.pop(0)
print(ans)    
  

