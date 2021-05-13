W,H,x,y,rad = (int(x) for x in input().split())

t = y + rad
b = y - rad
r = x + rad
l = x - rad

if (t > H) or (b < 0) or (r > W) or (l < 0):
  print ("No")
else:
  print ("Yes")
