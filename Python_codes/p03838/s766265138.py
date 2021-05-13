x, y=map(int, input().split())
c1=x<=y
c2=x*y>=0
a=0
if c1 and c2: # 正正か負負でｘ＜Y
  print(y-x)
elif c1 and not c2: # 負正でx<y
  print(abs(y-abs(x))+1)
elif not c1 and c2: # 正正か負負でx>y
  if x*y==0:
    a=1
  else:
    a=2
  print(x-y+a)
elif not c1 and not c2: # 正負でx>y
  print(abs(x-abs(y))+1)
