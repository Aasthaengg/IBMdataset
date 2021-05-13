a,b = map(int, input().split())

x = (a+b)/2
 
if x == int(x):
  print(int(x))
 
else:
  x += 1
  print(int(x))
