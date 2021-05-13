n = input()
s = list(map(str,input().strip().split()))

from collections import deque

d = deque()

for i,_s in enumerate(s):
  if i % 2 == 0:
    d.appendleft(_s)
  else:
    d.append(_s)
if len(s) %2 != 0:
  print(" ".join(list(d)))
else:
  print(" ".join(list(deque(reversed(d)))))