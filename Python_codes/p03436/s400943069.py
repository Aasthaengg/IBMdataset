from collections import deque
import sys
input = sys.stdin.readline

h,w = map(int,input().split())
MAP = [list(input().rstrip()) for i in range(h)]  #rstripで最後の/nを省ける
sharp = 0
for i in range(h):
  sharp += MAP[i].count("#")
#print(sharp)

#必要なもの MAP(list), MOVE(list), STACK(deque)
MAP[0][0]=1
MOVE = [[1,0],[-1,0],[0,1],[0,-1]]
STACK = deque([(0,0)])
while STACK:
  y, x = STACK.popleft()
  for dy,dx in MOVE:
    ny = y + dy
    nx = x + dx
    if not(0 <= ny < h) or not(0 <= nx < w) or MAP[ny][nx]!='.':
      continue
    else:
      STACK.append((ny,nx))
      MAP[ny][nx] = MAP[y][x] + 1


if type(MAP[h-1][w-1]) == int:
  ans = h*w -MAP[h-1][w-1]-sharp
else:
  ans = -1
    
print(ans)