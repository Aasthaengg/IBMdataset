from collections import deque
n = int(input())
a = list(map(int, input().split()))

q = deque()
t = 0
for i in a:
  if t == 0: q.append(i)
  else: q.appendleft(i)
  t = -1 - t
  
if t == 0: print(*q)
else: print(*reversed(q))