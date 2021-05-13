n = int(input())
a = list(map(int,input().split()))
d = {}
for ai in a:
  if ai in d:
    d[ai] += 1
  else:
    d[ai] = 1
d = sorted(d.items(),reverse = True)
r = []
for k,v in d:
  if len(r) >= 2:
    break
  if v >= 4:
    r.append(k)
    r.append(k)
  elif v >= 2:
    r.append(k)
if len(r) < 2:
  print(0)
else:
  print(r[0]*r[1])
