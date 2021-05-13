from collections import deque
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = deque()
y = 0
while y < H:
  x = 0 if y % 2 == 0 else W-1
  dx = 1 if y % 2 == 0 else -1
  d = 0
  while dx > 0 and x < W-1 or dx < 0 and x > 0:
    if A[y][x] % 2 == 1:
      ans.append("%d %d %d %d"%(y+1, x+1, y+1, x+dx+1))
      A[y][x] -= 1
      A[y][x+dx] += 1
    x += dx
  if A[y][x] % 2 == 1 and y < H-1:
    ans.append("%d %d %d %d"%(y+1, x+1, y+2, x+1))
    A[y][x] -= 1
    A[y+1][x] += 1
  y += 1
print(len(ans))
print("\n".join(ans))