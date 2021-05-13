n,m,x,y=map(int,input().split())
xx=list(map(int,input().split()))
yy=list(map(int,input().split()))
mx=max(xx)
my=min(yy)
if mx>=my:
  print("War")
elif mx>=y or x>=my:
  print("War")
else:
  print("No War")