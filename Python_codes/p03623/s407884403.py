a,b,c=map(int,input().split())
d = int(b-a)
e = int(c-a)
if d < 0:
  d = -d

if e < 0:
  e = -e

if d > e:
  print("B")
else:
  print("A")
