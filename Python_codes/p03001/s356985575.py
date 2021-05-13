w,h,x,y = map(int, input().split())

ox = w/2
xy = h/2
s = w*h/2

if ox == x and xy == y:
  print(s, 1)

else:
  print(s, 0)