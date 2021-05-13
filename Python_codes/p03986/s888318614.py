from collections import deque
S = input()
d = deque()
for s in S:
  if len(d) == 0:
    d.append(s)
  elif s == "T":
    if d[-1] == "S":
      d.pop()
    else:
      d.append(s)
  elif s == "S":
    d.append(s)
print(len(d))