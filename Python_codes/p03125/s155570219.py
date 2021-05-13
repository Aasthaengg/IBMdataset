x,y = map(int,input().split())	
if y%x == 0:
  print(int(y+x))
else:
  print(int(y-x))