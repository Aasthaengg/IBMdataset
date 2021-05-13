a,b=map(int,input().split())
c=(a+b)/2
if c%1==0:
  print(int(c))
else:
  print(int((c//1)+1))