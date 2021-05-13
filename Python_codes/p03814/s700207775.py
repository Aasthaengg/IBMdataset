from collections import deque
s = deque(list(input()))
while True:
  if s.popleft()=="A":
    break
while True:
  if s.pop()=="Z":
    break
print(len(s)+2)