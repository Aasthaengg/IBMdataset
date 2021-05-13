from collections import deque
s = input()
q = int(input())

s = deque(s)
t = 0
for _ in range(q):
  query = list(map(str, input().split()))
  if query[0] == "1": t = 1 - t
  else:
    if t == 0:
      if query[1] == "1": s.appendleft(query[2])
      elif query[1] == "2": s.append(query[2])
    elif t == 1:
      if query[1] == "1": s.append(query[2])
      elif query[1] == "2": s.appendleft(query[2])
if t == 1:print("".join(s)[::-1])
else: print("".join(s))