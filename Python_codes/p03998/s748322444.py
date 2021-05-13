a=input()
b=input()
c=input()
from collections import deque
da=deque(list(a))
db=deque(list(b))
dc=deque(list(c))
now=da.popleft()
while (1):
  if now=="a":
    if da:
      now=da.popleft()
    else:
      break
  elif now=="b":
    if db:
      now=db.popleft()
    else:
      break
  elif now=="c":
    if dc:
      now=dc.popleft()
    else:
      break
print(now.upper())