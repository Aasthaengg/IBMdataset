x,y=map(int,input().split())
if x>=y and x%y==0:
  print(-1)
elif x<y:
  print(x)
else:
  print(x*y-x)
