W,H,x,y = map(int,input().split())

n = (W*H)/2
if W == x*2 and H == y*2:
  print(n, 1)
else:
  print(n, 0)
