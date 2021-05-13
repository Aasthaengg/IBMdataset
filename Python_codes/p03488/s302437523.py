slist=list(input())
x,y=map(int,input().split())

direction_x=True
xlist,ylist=[],[]
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

x-=xlist.pop(0)
#print(x,y,xlist,ylist)

# check each x,y
set_x={0}
for i in range(len(xlist)):
  new_set_x=set()
  for xx in set_x:
    new_set_x.add(xx+xlist[i])
    new_set_x.add(xx-xlist[i])
  set_x=new_set_x
    
set_y={0}
for i in range(len(ylist)):
  new_set_y=set()
  for yy in set_y:
    new_set_y.add(yy+ylist[i])
    new_set_y.add(yy-ylist[i])
  set_y=new_set_y

#print(set_x,set_y)
if x in set_x and y in set_y:
  print("Yes")
else:
  print("No")