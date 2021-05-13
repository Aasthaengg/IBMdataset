from collections import deque
n=int(input())
S=list(input().split())[::-1]
b=deque([])
for i in range(n//2):
  b.append(S.pop())
  b.appendleft(S.pop())
if n%2:
  b.append(S.pop())
  print(' '.join(list(b)[::-1]))
else:print(' '.join(list(b)))