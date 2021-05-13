
x,y = map(int,input().split())
d = x % y
d_ = y - d
if d > d_:
  print(d_)
else:
  print(d)