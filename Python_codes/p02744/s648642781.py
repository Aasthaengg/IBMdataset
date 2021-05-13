from collections import deque

N = int(input())
if N == 1:
  print('a')
  exit()

h = deque(['a'])

while h:
  s = h.pop()
  if len(s) == N:
    print(s)
  else:
    a = set([])
    for i in s:
      a.add(i)
    for i in range(len(a),-1,-1):
      h.append(s+chr(ord('a')+i))