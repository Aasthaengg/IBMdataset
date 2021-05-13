n,p = map(int,input().split())
x = 1
y = 0
a = list(map(int,input().split()))
for ai in a:
  if ai%2 == 0:
    x += x
    y += y
  else:
    t = x
    x += y
    y += t
if p == 0:
  print(x)
else:
  print(y)