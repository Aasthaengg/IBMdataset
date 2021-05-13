import copy
a = list(input())
if len(a) == 5:
  print("No")
  exit()
else:
  b = copy.copy(a)
  b.reverse()
  x = int((len(a)/2))
  for i in range(x):
    if a[i] != b[i]:
      print("No")
      exit()
  c = a[:x]
  d = a[x+1:]
  y = int((len(c)/2))
  for i in range(y):
    if c[i] != c[-(i+1)] or d[i] != d[-(i+1)]:
      print("No")
      exit()
  print("Yes")