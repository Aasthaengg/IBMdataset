H,W = map(int,input().split())
l = [[]]
for i in range(H):
  l.append([0]+list(map(int,input().split())))

ans = []
y = 1
x = 1
xstock = 0
ystock = 0
seen = [[False for i in range(W+2)] for j in range(H+2)]
seen[1][1] = True

while True:
  if xstock > 0 and ystock > 0:
    ans.append([ystock,xstock,y,x])
    xstock = x 
    ystock = y
  if l[y][x]%2 == 1:
    if xstock == 0 and ystock == 0:
      xstock = x 
      ystock = y
    elif xstock > 0 and ystock > 0:
      xstock = 0
      ystock = 0
  #マス目の移動
  #右
  if x+1 <= W and seen[y][x+1] == False:
    x = x+1
    y = y
    seen[y][x] = True
    continue
  #左
  elif x-1 >= 1 and seen[y][x-1] == False:
    x = x-1
    y = y
    seen[y][x] = True
    continue
  #下
  elif y+1 <= H:
    x = x
    y = y+1
    seen[y][x] = True
    continue
  #止まったら
  break
###
N = len(ans)
print(N)
for i in range(N):
  print(*ans[i])   