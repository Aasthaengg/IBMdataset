n,a,b=map(int,input().split())
x=a+b-n
if x>=0:
  x+=0
else:
  x=0
  
print(min(a,b),x)  