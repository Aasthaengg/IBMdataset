S = input()
X,Y = map(int,input().split())

x = True # x軸方向を向いている

Slist = []
import itertools
for key,g in itertools.groupby(S):
  num = len(list(g))
  Slist.append((key, num))
  
xdp = set()
ydp = set([0])
ind = 0

if Slist[0][0] == "F":
  xdp.add(Slist[0][1])
  ind += 1
else:
  xdp.add(0)
  
for i in range(ind, len(Slist)):
  if Slist[i][0] == "T":
    if Slist[i][1] % 2 == 1:
      x ^= True
    continue
  step = Slist[i][1]
  if x:
    next_dp = set()
    for xpos in xdp:
      next_dp.add(xpos + step)
      next_dp.add(xpos - step)
    xdp = next_dp
  else:
    next_dp = set()
    for ypos in ydp:
      next_dp.add(ypos + step)
      next_dp.add(ypos - step)
    ydp = next_dp
    
if X in xdp and Y in ydp:
  print("Yes")
else:
  print("No")