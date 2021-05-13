a,b=input().split()
a=int(a)
b=int(b)
c=list(map(int,input().split()))
c.sort()
d=sum(c)
e=0
if a<=b:
  print(0)
else:
  for i in range(1,b+1):
    e=e+c[-i]
  print(d-e)