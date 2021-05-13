# import itertools
# import pprint
import copy
from collections import deque

gem,ope = map(int,input().split())
vlist = deque(map(int,input().split()))

ans = 0

for l in range(ope+1):
  for r in range(ope-l+1):
    if l+r>ope or l+r>gem:
      break

    x   = ope-l-r
    now = []
    deq = copy.copy(vlist) 

    for i in range(l):
      now.append(deq.popleft())
    for j in range(r):
      now.append(deq.pop())
    for k in range(x):
      if now==[]:
        break
      if min(now)<0:
        now.remove(min(now))
    
    if ans<sum(now):
      ans = sum(now)

print(ans)
