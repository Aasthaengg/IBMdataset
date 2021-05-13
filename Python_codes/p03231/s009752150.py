from collections import defaultdict
import math
n,m = map(int, input().split())
s = input()
t = input()

ans = int((n*m)/math.gcd(n,m))
d = defaultdict(int)
if n > m:
  for i in range(n):
    if i == 0:
      d[1] = s[i]
    else:
      d[i*int(ans/n)+1] = s[i]
  ng = 0
  for i in range(m):
    if i == 0:
      if d[1] != t[i]:
        ng += 1
    else:
      if d[i*int(ans/m)+1] != 0 and d[i*int(ans/m)+1] != t[i]:
        ng += 1
else:
  for i in range(m):
    if i == 0:
      d[1] = t[i]
    else:
      d[i*int(ans/m)+1] = t[i]
  ng = 0
  for i in range(n):
    if i == 0:
      if d[1] != s[i]:
        ng += 1
    else:
      if d[i*int(ans/n)+1] != 0 and d[i*int(ans/n)+1] != s[i]:
        ng += 1
if ng > 0:
  print (-1)
else:
  print (ans)