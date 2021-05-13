import math
n,k,*a = map(int,open(0).read().split())
a = list(set(a))
if k in a:
  print("POSSIBLE")
elif k>max(a):
  print("IMPOSSIBLE")
else:
  b = max(a)-k
  c = a.pop()
  for i in a:
    c = math.gcd(c,i)
    if c == 1:
      break
  if b%c == 0:
    print("POSSIBLE")
  else:
    print("IMPOSSIBLE")