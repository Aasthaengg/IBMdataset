from operator import itemgetter

n = int(input())
xyh = sorted([list(map(int, input().split())) for i in range(n)], key = itemgetter(2),reverse=True)
X,Y,H = xyh[0][0],xyh[0][1],xyh[0][2]
if n == 1:
  print(X,Y,H)
  exit()
for cx in range(101):
  for cy in range(101):
    height = abs(cx-X) + abs(cy-Y) + H
    for x,y,h in xyh[1:]:
      if h != max(0, height - abs(cx-x) - abs(cy-y)):
        break
    else:
      print(cx,cy,height)
      exit()