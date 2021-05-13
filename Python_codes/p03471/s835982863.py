N,Y=map(int,input().split())

for x in range(Y//10000+3):
  for y in range(Y//5000+3):
    z = N-x-y
    if z < 0:break
    SUM = 10000*x + 5000*y + 1000*z
    if SUM == Y:
      print(x,y,z)
      exit()
    elif SUM > Y:break
print(-1,-1,-1)