import math
n,x = (int(x) for x in input().split())
l = []
for i in range (n):
  m = int (input ())
  x -= m
  l.append (m)
list.sort (l)
a = math.floor (x / l[0])
print (n+a)