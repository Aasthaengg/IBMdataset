a, b = map(int,input().split())

if a >= 13:
  print(b)
  exit()
  
if a >= 6:
  b //= 2
  print(b)
  exit()
  

print(0)
