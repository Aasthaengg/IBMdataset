import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
d = {}
m = 0
for e in c:
  m += (c[e] * (c[e] - 1) // 2)
  if c[e] == 1:
    d[e] = 0
  elif c[e] == 2:
    d[e] = 1
  else:
    d[e] = (c[e] * (c[e] - 1) // 2) - ((c[e] - 1) * (c[e] - 2) // 2)
for i in range(n):
  print(m - d[a[i]])