from collections import deque
S = input()
d = deque()
for s in S:
  if len(d) == 0:
    d.append(s)
  elif s == "T":
    d.pop() if d[-1] == "S" else d.append(s)
  elif s == "S":
    d.append(s)
print(len(d))