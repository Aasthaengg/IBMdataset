W,H,x,y = map(int, input().split())

area = str(W * H / 2)
if W / 2 == x and H / 2 == y:
  center = '1'
else:
  center = '0'
  
print(area + ' ' + center)