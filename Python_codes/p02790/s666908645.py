a,b=input().split()
c=""
i=0
if int(a)>=int(b):
  while i<int(a):
    c=c+b
    i=i+1
  print(c)
else:
  while i<int(b):
    c=c+a
    i=i+1
  print(c)