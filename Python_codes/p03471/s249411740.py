n,Y=map(int,input().split())

for x in range(n+1):
  for y in range(n+1):
    z = 0 if n-x-y <= 0 else n-x-y
    if 10000*x + 5000*y + 1000*(z) == Y and x+y+z == n:
      print(x,y,z)
      exit()
print(-1,-1,-1)