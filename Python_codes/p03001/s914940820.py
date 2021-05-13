W,H,x,y = map(int,input().split())

area = W*H/2
if  x==W/2 and y==H/2:
  print('{:.06f}'.format(area),"1")
else:
  print('{:.06f}'.format(area),"0")