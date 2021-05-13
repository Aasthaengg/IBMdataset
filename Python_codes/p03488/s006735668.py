str = input()
x,y = map(int,input().split())
dx,dy = 0,0

fn = [len(n) for n in str.split("T")]
dir = [[],[]]

for i in range(len(fn)):
  dir[i%2].append(fn[i])

xdir = dir[0]
ydir = dir[1]

dx = xdir.pop(0)
xdir.sort()
while xdir != []:
  if dx < x:
    dx += xdir.pop()
  else:
    dx -= xdir.pop()
    
ydir.sort()
while ydir != []:
  if dy < y:
    dy += ydir.pop()
  else:
    dy -= ydir.pop()

if dx == x and dy == y:
  print("Yes")
else:
  print("No")