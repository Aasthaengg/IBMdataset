a,b,c=map(int,input().split())
d=max(a,b,c)
s=a+b+c
if d%2==0 and s%2==0:
  print((3*d-a-b-c)//2)
elif d%2==1 and s%2==1:
  print((3*d-a-b-c)//2)
else:
  print((3*(d+1)-a-b-c)//2)