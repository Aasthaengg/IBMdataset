a,b,c=map(int,input().split())
m=max(a,b,c)
a=m-a
b=m-b
c=m-c
if (a+b+c)%2==0:
  print((a+b+c)//2)
else:
  print((a+b+c)//2+2)