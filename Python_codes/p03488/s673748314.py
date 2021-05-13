S = input()
X,Y = map(int,input().split())

# [文字,その文字が連続する数]
from collections import deque
sumS = deque()
import itertools
for key,g in itertools.groupby(S):
  sumS.append([key,len(list(g))])
  
startx = 0 # Fで始まる場合はX軸の正の方向にあらかじめ進めて置く
# 最初のTが出るまではX軸正の方向に進む
if sumS[0][0] == "F":
  startx = sumS[0][1]
  sumS.popleft()

xdir = True # X軸方向を向いている
dpXcur = set()
dpXcur.add(startx)
dpYcur = set()
dpYcur.add(0) # Y軸は必ず0から始まる
dpXnex = set()
dpYnex = set()
while sumS:
  mark, steps = sumS.popleft()
  if mark == "F":
    if xdir: # X軸方向を向いている場合
      for x in dpXcur:
        dpXnex.add(x + steps)
        dpXnex.add(x - steps)
      dpXcur = dpXnex
      dpXnex = set()
    else:
      for y in dpYcur:
        dpYnex.add(y + steps)
        dpYnex.add(y - steps)
      dpYcur = dpYnex
      dpYnex = set()
  elif mark == "T":
    if steps % 2 == 1:
      # 奇数回の場合はX/Y軸の切り替え (偶数回の場合は何も起こらない)
      xdir ^= True
      
if X in dpXcur and Y in dpYcur:
  print("Yes")
else:
  print("No")
