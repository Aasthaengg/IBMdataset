import sys
l=[]
for i in sys.stdin:
  l.append(int(i))
print("Hello World" if l[0]==1 else l[1]+l[2])