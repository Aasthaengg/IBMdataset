N = int (input ())
l = {}
for i in range (N):
  a = int (input ())
  l[i+1] = a
b = 1
x = 0
for i in range (N+1):
  b = l[b]
  x += 1
  if b == 2:
    print (x)
    x = 0
    break
if x != 0:
  print (-1)