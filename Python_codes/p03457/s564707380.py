n = int(input())
x,y,t=0,0,0

for i in range(n):
  mt,mx,my= map(int,input().split())
  ft = mt - t
  fx = abs(x-mx)
  fy = abs(y-my)
  if fx + fy > ft:
    print("No")
    exit()
  elif (ft - (fx + fy)) % 2 == 0:
    pass
  else:
    print("No")
    exit()
  x,y,t=mx,my,mt
print("Yes")