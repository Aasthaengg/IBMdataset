from math import ceil
from collections import deque

N, D, H = map(int, input().split())
Monsters = sorted([list(map(int, input().split())) for i in range(N)])
Monsters = [[x, ceil(h/H)] for x, h in Monsters]

ans = 0
acc = 0
deq = deque([])

for x, h in Monsters:
  while deq and x>deq[0][0]:
    lim, dam = deq.popleft()
    acc -= dam
  c = max(0, h-acc)
  ans += c
  acc += c
  if c:
    deq += [(x+2*D, c)]
    
print(ans)