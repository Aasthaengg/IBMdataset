x,y,z = map(int, input().split())

if x == y == z:
  print("No")
elif x == y or y ==z or z ==x:
  print("Yes")
else:
  print("No")