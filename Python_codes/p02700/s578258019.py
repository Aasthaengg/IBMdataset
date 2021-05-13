a,b,c,d=map(int,input().split())
if a%d>0:
   a=a//d+1
elif a%d==0:
   a=a//d
if c%b>0:
  c=c//b+1
elif c%b==0:
  c=c//b
if a>=c:
  print("Yes")
else:
  print("No")
  
  
