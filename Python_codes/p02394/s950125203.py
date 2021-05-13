W, H, x, y, r = [int(i) for i in input().split()]

if x - r >= 0 and x + r <= W and y + r <= H and y - r >=0:
   print("Yes")

else:
   print("No")