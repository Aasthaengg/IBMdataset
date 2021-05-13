import sys

[Width, Height, x, y, r] = [int(x) for x in sys.stdin.readline().split()]

lower_x = r
lower_y = r
upper_x = Width - r
upper_y = Height -r 

if lower_x <= x <= upper_x and lower_y <= y <= upper_y:
   print("Yes")
else:
   print("No")