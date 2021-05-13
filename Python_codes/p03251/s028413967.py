n,m,x,y=map(int,input().split())
xl=list(map(int,input().split()))
yl=list(map(int,input().split()))
a=max(x,max(xl))
b=min(y,min(yl))
if b-a<=0:
  print('War')
else:
  print('No War')