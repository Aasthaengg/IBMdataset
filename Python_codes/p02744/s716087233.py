n=int(input())
from collections import deque
def dfs():
  todo=deque([[1]])
  ret=[]
  while len(todo)>0:
    t=todo.popleft()
    if len(t)==n:
      ret.append(t)
    else:
      l=max(t)+1
      for i in range(l):
        tc=t.copy()
        tc.append(i+1)
        todo.append(tc)
  return ret
a=dfs()
n2a = lambda c: chr(c+64).lower()
for ai in a:
  #print(ai)
  print(''.join(map(n2a,ai)))
