import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n,m = map(int,readline().split())
c = set()
v = {}
for i in range(m):
  a,b = map(int,readline().split())
  d = list(map(int,readline().split()))
  e = 0
  for j in d:
    e += 2**(j-1)
  if i >= 1:
    s = list(c)
    for k in s:
      if not k|e in c:
        c.add(k|e)
        v[k|e] = a+v[k]
      else:
        v[k|e] = min(v[k|e],a+v[k])
  if not e in c:
    c.add(e)
    v[e] = a
  else:
    v[e] = min(v[e],a)
    
if 2**n-1 in c:
  print(v[2**n-1])
else:
  print(-1)
