w,h,x,y,r = [int(s) for s in input().split(" ")]
if 0 <= (x - r) and 0 <= (y - r) and (x + r) <= w and (y + r) <= h:
  print("Yes")
else:
  print("No")