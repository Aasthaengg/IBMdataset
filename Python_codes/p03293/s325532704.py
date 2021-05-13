from collections import deque
s,t=deque([*input()]),deque([*input()])
for _ in range(len(s)):
  if s==t: print('Yes');break
  s.rotate(1)
else:
  print('No')