n,m,x,y=map(int,input().split())
x,y=[x],[y]
x.extend(list(map(int,input().split())))
y.extend(list(map(int,input().split())))
x.sort()
y.sort()
if x[-1]>=y[0]:
  print('War')
else:
  print('No War')