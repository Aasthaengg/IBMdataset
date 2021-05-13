x,y = map(int,input().split())
if x == 1 and y == 1:
  print(1000000)
elif x < 4 and y > 3:
  print(100000*(4-x))
elif x > 3 and y < 4:
  print(100000*(4-y))
elif x < 4 and y < 4:
  print(100000*(8-x-y))
else:
  print(0)