a,b,x=map(int,input().split())
if a%x!=0:
  a+=x-a%x

if a==b and a==0:
  print(1)
elif a==b and a==x:
  print(1)
elif a>=b:
  print(0)
else:
  print(b//x-a//x+1)