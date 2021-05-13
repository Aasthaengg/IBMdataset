from collections import deque

n = int(input())
A = deque()

for i in range(n):
  order = input().split()
  if order[0] == "insert":
    A.appendleft(order[1])
  elif order[0] == "delete":
    try:
      A.remove(order[1])
    except ValueError:
      pass
  elif order[0] == "deleteFirst":
    A.popleft()
  elif order[0] == "deleteLast":
    A.pop()

print(" ".join(map(str, A)))

