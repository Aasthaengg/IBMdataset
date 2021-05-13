a,b,c,d=map(int,input().split())
flag=True
if abs(a-b)>d:
  flag=False
if abs(b-c)>d:
  flag=False

if abs(a-c)<=d:
  flag=True
if flag:
  print("Yes")
else:
  print("No")