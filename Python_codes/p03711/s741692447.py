import sys
gp_a = [1,3,5,7,8,10,12]
gp_b = [4,6,9,11]

x, y = list(map(int, input().split()))

if x == 2 or y == 2:
  print("No")
  sys.exit()
if (x in gp_a) and (y in gp_a):
  print("Yes")
elif (x in gp_b) and (y in gp_b):
  print("Yes")
else:
  print("No")