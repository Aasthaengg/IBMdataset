s = input()
x, y = map(int, input().split())

S = list(map(len, s.split("T")))
Sx = []
Sy = []

for i in range(len(S)):
  if i % 2 == 0:
    Sx.append(S[i])
  else:
    Sy.append(S[i])

maxX = sum(Sx)
maxY = sum(Sy)

setX = set([maxX])
flg = True
for i in Sx:
  if flg:
    #初手だけはXの正方向にしかすすめない
    flg = False
    continue
  li = list(setX)
  for a in li:
    setX.add(a - 2*i)
    
setY = set([maxY])
for i in Sy:
  li = list(setY)
  for a in li:
    setY.add(a - 2*i)
    
if x in setX and y in setY:
  print("Yes")
else:
  print("No")