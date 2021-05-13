from collections import deque
S = input()
stack = deque([])
c = 0
for s in S:
  if len(stack)==0:
    stack.append(s)
  elif stack[-1]==s:
    stack.append(s)
  else:
    stack.pop()
    c += 2
print(c)