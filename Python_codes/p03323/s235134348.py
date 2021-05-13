a,b = map(int,input().split())
c = abs(a-b)
d = 16 - a - b

if c * 2 > d:
  print(":(")
  
else:
  print("Yay!")
