s = int(input().strip())
m = int(1e9)
if s % m == 0:
  x = 0
  y = s//m
else:
  x = m-(s%m)
  y = (s//m)+1
print(0,0,1000000000,1,x,y)
