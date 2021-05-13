p = int(input())
c1 = int(input())

change = p % 500

if (change == 0) or (c1 > change):
  print("Yes")
else:
  print("No")