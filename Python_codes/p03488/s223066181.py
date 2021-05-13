import sys
readline = sys.stdin.readline

S = readline().rstrip()
gx,gy = map(int,readline().split())

C = []

import itertools
for key,g in itertools.groupby(S):
  C.append([key,len(list(g))])
  
x,y = 0,0
ind = 0
if C[0][0] == "F":
  x += C[0][1]
  ind = 1

# Xの方向を向いている
dirX = True
now_x = {x}
now_y = {y}
for i in range(ind,len(C)):
  if C[i][0] == "F":
    step = C[i][1]
    if dirX:
      nex_x = set()
      for n in now_x:
        nex_x.add(n + step)
        nex_x.add(n - step)
      now_x = nex_x
    else:
      nex_y = set()
      for n in now_y:
        nex_y.add(n + step)
        nex_y.add(n - step)
      now_y = nex_y
  else:
    if C[i][1] % 2 == 1:
      dirX ^= True
    
if gx in now_x and gy in now_y:
  print("Yes")
else:
  print("No")
