N = int(input())
A = list(map(int, input().split()))
d = {}
for a in A:
  d[a] = d.get(a, 0) + 1
d2 = sorted(d.items(), reverse = True)
s = 0
t = 0
f = 0
for p in d2:
  if s == 0:
    if p[1] >= 4:
      print(p[0] * p[0])
      f = 1
      break
    elif p[1] >= 2:
      s = p[0]
  else:
    if p[1] >= 2:
      print(s * p[0])
      f = 1
      break
if f == 0:
  print(0)