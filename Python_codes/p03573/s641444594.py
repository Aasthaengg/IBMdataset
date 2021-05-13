a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
ls=[a,b,c]
ls.sort()
if ls[0]==ls[1]:
  print(ls[2])
else:
  print(ls[0])