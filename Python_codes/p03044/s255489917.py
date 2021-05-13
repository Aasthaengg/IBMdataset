from collections import deque

N = int(input())
dic = {i:[] for i in range(1,N+1)}

for _ in range(N-1):
  u, v, w = map(int, input().split())
  dic[u].append((v,w))
  dic[v].append((u,w))
  
s1 = set([1])
s2 = set([])
h = deque([(1,0)])

while h:
  p = h.popleft()
  for t in dic[p[0]]:
    if t[0] == p[1]:
      continue
    if t[1]%2 == 0:
      if p[0] in s1:
        s1.add(t[0])
      else:
        s2.add(t[0])
    else:
      if p[0] in s1:
        s2.add(t[0])
      else:
        s1.add(t[0])
    h.append((t[0],p[0]))

for i in range(1,N+1):
  if i in s1:
    print(0)
  elif i in s2:
    print(1)