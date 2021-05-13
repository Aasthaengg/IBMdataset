import sys
l=[]
for i in sys.stdin:
  l.append(int(i))
if l[0]==1:
  print("Hello World")
else:
  print(l[1]+l[2])