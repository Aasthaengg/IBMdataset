from collections import deque
n = int(input())
a = list(map(int, input().split()))

d = deque()
t = 0
for i in a:
  if t == 0: d.append(i)
  elif t == 1: d.appendleft(i)
  t = 1 - t
  
if t == 0: print(*d)
else: print(*list(reversed(d)))