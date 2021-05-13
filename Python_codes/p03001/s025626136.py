w,h,x,y=map(int,input().split())

x_mid = w / 2
y_mid = h / 2
if x_mid == x and y_mid == y:
  flg = 1
else:  
  flg = 0
print(w*h/2,flg)