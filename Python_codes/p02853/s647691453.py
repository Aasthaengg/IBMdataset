x,y = map(int,input().split())
if x + y == 2:
  print(1000000)
elif x + y == 3:
  print(500000)
elif x + y == 5:
  print(300000)
elif x + y == 4:
  print(400000)
elif x + y == 6:
  print(200000)
elif x + y >=5 and min(x,y) == 1:
  print(300000)
elif x + y >=5 and min(x,y) == 2:
  print(200000)
elif x + y >=5 and min(x,y) == 3:
  print(100000)
else:
  print(0)