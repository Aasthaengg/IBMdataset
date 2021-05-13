W,H,x,y = (int(x) for x in input().split())
if W%2 == 0 and H%2 == 0 and x == int(W/2) and y == int(H/2):
  print(W*H/2,1)
else:
  print(W*H/2,0)