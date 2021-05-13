MM = input().split()
W = int(MM[0])
H = int(MM[1])
N = int(MM[2])
a = 0
b = 0
c = W
d = H
for i in range(N):
  LL = input().split()
  x = int(LL[0])
  y = int(LL[1])
  aa = int(LL[2])
  if aa == 1:
    if x > a:
      a = x
  elif aa == 2:
    if x < c:
      c = x
  elif aa == 3:
    if y > b:
      b = y
  else:
    if y < d:
      d  = y

if (c-a) > 0 and (d -b) > 0:
  ans = (c-a) * (d -b)
  print(ans)
else:
  print(0)