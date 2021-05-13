N = int(input())

locx = 0
locy =0
time = 0
for i in range(N):
  t,x,y = map(int,input().split())
  time = t-time
  dis = abs(locx-x)+abs(locy-y)
  if (time-dis)<0 :
    print("No")
    exit()
  if (time-dis)%2 == 1:
    print("No")
    exit()
    
  
  time = t
  locx = x
  locy = y
    
  
else :
  print("Yes")