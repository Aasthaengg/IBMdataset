import sys
readline = sys.stdin.readline

S = readline().rstrip()
X,Y = map(int,readline().split())

# ("指示","回数")の形式に変換する
C = [] 
import itertools
for key,g in itertools.groupby(S):
  C += [[key,len(list(g))]]

x = 0
y = 0
ind = 0
if C[0][0] == "F": # 最初からX軸方向に進む場合
  x += C[0][1]
  ind += 1

# X軸方向を向いている
dirX = True

Xset = {x}
Yset = {y}

for i in range(ind, len(C)):
  command, num = C[i]
  if command == "F":
    if dirX:
      next_Xset = set()
      for x in Xset:
        next_Xset.add(x + num)
        next_Xset.add(x - num)
      Xset = next_Xset
    else:
      next_Yset = set()
      for y in Yset:
        next_Yset.add(y + num)
        next_Yset.add(y - num)
      Yset = next_Yset
  else:
    if num % 2 == 1:
      dirX ^= True

if X in Xset and Y in Yset:
  print("Yes")
else:
  print("No")
