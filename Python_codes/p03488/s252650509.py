slist=list(input())
x,y=map(int,input().split())

vec=[(1,0),(0,1),(-1,0),(0,-1)]

direction_x=True
xlist=[]
ylist=[]
cnt=0
for s in slist:
  if s=="F":
    cnt+=1
  else:
    if direction_x:
      xlist.append(cnt)
    else:
      ylist.append(cnt)
    cnt=0     
    direction_x=not direction_x
else:
  if direction_x:
    xlist.append(cnt)
  else:
    ylist.append(cnt)

x-=xlist[0]
xlist=xlist[1:]
#print(x,y,xlist,ylist)

# check each x,y
dp_x=[]
for _ in range(len(xlist)+1):
  dp_x.append(set())
dp_x[0]={0}
for i in range(1,len(xlist)+1):
  for j in dp_x[i-1]:
    dp_x[i].add(j+xlist[i-1])
    dp_x[i].add(j-xlist[i-1])
#print(dp_x)

dp_y=[]
for _ in range(len(ylist)+1):
  dp_y.append(set())
dp_y[0]={0}
for i in range(1,len(ylist)+1):
  for j in dp_y[i-1]:
    dp_y[i].add(j+ylist[i-1])
    dp_y[i].add(j-ylist[i-1])
#print(dp_y)

#print(dp_x,dp_y)
if x in dp_x[-1] and y in dp_y[-1]:
  print("Yes")
else:
  print("No")