import heapq
from operator import itemgetter

n,k = map(int, input().split())
td = sorted([list(map(int, input().split())) for i in range(n)],key=itemgetter(1),reverse=True)
neta = [0] * (n+1)
hq = []
kind = 0
ans = 0
for t,d in td[:k]:
  if neta[t]:
    hq.append(d)
  else:
    kind += 1
  neta[t] += 1
  ans += d
ans += kind ** 2
heapq.heapify(hq)
now = k
new_ans = ans
while hq and now < n:
  t,d = td[now][0],td[now][1]
  if not neta[t]:
    MIN = heapq.heappop(hq)
    new_ans += d - MIN + 2 * kind + 1
    ans = max(ans,new_ans)
    kind += 1
    neta[t] += 1
  now += 1	
print(ans)