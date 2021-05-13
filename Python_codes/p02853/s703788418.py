x,y = map(int, input().split()) 
ans = 0

if x == 1 and y == 1:
  print(10**6)
else:

  x = 0 if x >= 4 else 4 - x
  y = 0 if y >= 4 else 4 - y
  print(x*10**5 + y*10**5)
  

