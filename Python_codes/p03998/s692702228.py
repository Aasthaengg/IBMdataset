from collections import deque
A, B, C = map(deque, (input(), input(), input()))
d = {'a':A, 'b':B, 'c':C}
c = 'a'
while True:
  X = d[c]
  if not X:
    print(c.upper())
    exit()
  c = X.popleft()
