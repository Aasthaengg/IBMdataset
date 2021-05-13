W,H,N=map(int,input().split())
# Wはx軸、Hはy軸
x_s=0
x_g=W
y_s=0
y_g=H

for i in range(N):
  x,y,a=map(int,input().split())
  # aが1ならxの始点がxiになる
  # aが2ならxの終点がxiになる
  # aが3ならyの始点がyiになる
  # aが4ならyの始点がyiになる
  if a==1:
    if x_s<x:x_s=x
  elif a==2:
    if x_g>x:x_g=x
  elif a==3:
    if y_s<y:y_s=y
  else:
    if y_g>y:y_g=y
if (x_g-x_s) <= 0 or (y_g-y_s)<= 0:
  print(0)
else:
  print((x_g-x_s)*(y_g-y_s))
