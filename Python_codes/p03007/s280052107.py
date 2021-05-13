N = int(input())
a = list(map(int, input().split()))
p = [t for t in a if t >= 0]
m = [t for t in a if t < 0]
p.sort(reverse = True)
m.sort()
l = []
if N == 2:
  print(max(a) - min(a))
  print(max(a), min(a))
  exit(0)
if len(p) == 0:
  u = m.pop()
  v = m.pop()
  l.append((u, v))
  p.append(u - v)
if len(m) == 0 and len(p) >= 2:
  u = p.pop()
  v = p.pop()
  l.append((u, v))
  m.append(u - v)
while len(p) >= 2:
  u = m.pop()
  v = p.pop()
  l.append((u, v))
  m.append(u - v)
while len(m):
  t = p[0]
  u = m.pop()
  l.append((t, u))
  p[0] = t - u
print(p[0])
for res in l:
  print(*res)