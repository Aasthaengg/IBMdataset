a,b,c,d,e,f=map(int,input().split())
res=-1
ans=[0,0]
s1=set()
s2=set()
for x in range(0,f+1,100*a):
  for y in range(0,f+1-x,100*b):
    s1.add(x+y)
for x in range(0,f+1,c):
  for y in range(0,f+1-x,d):
    s2.add(x+y)
for x in s1:
  for y in s2:
    if x*e/100>=y and 0<x+y<=f:
      tmp=y/(x+y)
      if tmp>res:
        res=tmp
        ans=[x+y,y]
print(*ans)