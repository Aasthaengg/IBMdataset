from collections import deque 
A=deque(list(input()))
B=deque(input())
C=deque(list(input()))
now='a'
while len(A)>=0 and len(B)>=0 and len(C)>=0:
  if now=='a':
    if A:
      now=A.popleft()
    else:
      print('A')
      exit()
  elif now=='b':
    if B:
      now=B.popleft()
    else:
      print('B')
      exit()
  else:
    if C:
      now=C.popleft()
    else:
      print('C')
      exit()