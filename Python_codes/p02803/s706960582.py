from collections import deque
import copy
H, W = map(int, input().split())
 
start = set()
for y in range(H):
  for x, w in enumerate(input()):
    if w == '.':
      start.add((x,y))

score = 0
ssize = [(-1,0),(0,-1),(1,0),(0,1)]
for xy in start:
  d = deque()
  d.append((xy+(0,)))
  step = 0
  can = copy.deepcopy(start)
  can.remove(xy)
  while len(d) > 0:
    now = d.popleft()
    step = now[2]
    for xs, ys in ssize:
      nxt = (now[0]+xs, now[1]+ys)
      if nxt in can:
        d.append(nxt+(step+1,))
        can.remove(nxt)
  score = max(step, score)
  
print(score)