import math
n,k = map(int, input().split())
a = list(map(int, input().split()))

g = a[0]
for i in range(n):
  g = math.gcd(g,a[i])

if k%g == 0 and k <= max(a):
  print ('POSSIBLE')
else:
  print ('IMPOSSIBLE')