a,b=map(int,input().split())
c=list(map(int,input().split()))
d=sum(c)/(4*b)
e=[i for i in c if i<d]
if len(e)>a-b:
  print("No")
else:
  print("Yes")