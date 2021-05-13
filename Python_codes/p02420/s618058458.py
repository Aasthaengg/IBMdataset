from collections import deque
for str in iter(input, "-"):
  dq = deque(str)

  m = int(input())
  for _ in range(m):
    h = int(input())
    dq.rotate(-h)

  print("".join(dq))