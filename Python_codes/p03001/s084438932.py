
W,H,x,y = map(int,input().split())

  
if (x == W/2 or y == H/2 or y == -(H*x/W)+H or y == (H*x)/W):
  if x == W/2 and y == H/2:
    print(W*H/2,1)
  else:
    print(W*H/2,0)
elif (x == 0 or x == W) and (y == 0 or y == H):
  print(W*H/2,0) 
else:
  print(W*H/2,0)