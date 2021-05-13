a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=0
if a>=b:
  for i in range(101):
    if a%(b-i)==0 and b%(b-i)==0:
      d=d+1
      if d==c:
        print(b-i)
        break
if a<b:
  for i in range(101):
    if a%(a-i)==0 and b%(a-i)==0:
      d=d+1
      if d==c:
        print(a-i)
        break