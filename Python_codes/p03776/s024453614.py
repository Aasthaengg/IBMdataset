import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N, A, B = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse = True)
res = 0
xi = 0
xis = []
for i in range(A - 1, B):
  t = 0
  for j in range(i + 1): t += a[j]
  t /= i + 1
  if res < t:
    res = t
    xi = i + 1
    xis = [i + 1]
  elif res == t:
    xis.append(i + 1)
resc = 0
while len(xis):
  xi = xis.pop()
  d = dd(int)
  for x in a: d[x] += 1
  d2 = dd(int)
  for i in range(xi): d2[a[i]] += 1
  #print(d, d2)
  tt = 1
  for k in d2.keys():
    t = 1
    for i in range(d[k], 0, -1):
      if i <= d[k] - d2[k]: break
      t *= i
    for i in range(1, d2[k] + 1): t //= i
  #print(k, t, d[k], d2[k])
    tt *= t
  resc += tt

print(res)
print(resc)