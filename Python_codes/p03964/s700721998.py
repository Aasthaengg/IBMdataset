n=int(input())
x,y=1,1
for i in range(n):
  a,b=map(int,input().split())
  if x%a==0:
    x1=x//a
  else:
    x1=x//a+1
  if y%b==0:
    y1=y//b
  else:
    y1=y//b+1
  z1=max(x1,y1)
  x,y=a*z1,b*z1
print(x+y)