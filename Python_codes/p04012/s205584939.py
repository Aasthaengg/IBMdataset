a = input()
b = []
c = int(len(a))
import collections

for i in range(c):
  b.append(a[i])

d = collections.Counter(b)
e = []

for i in d.values():
  e.append(i)

f = int(len(e))
g = int(0)

for i in range(f):
  if int(e[i]) % 2 == 0:
    pass
  else:
    g = g + 1

if g == 0:
  print("Yes")
else:
  print("No")