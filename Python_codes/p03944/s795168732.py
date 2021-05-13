W, H, N = map(int, input().split())
left, right = 0, W
down, up = 0, H

for i in range(N):
  x, y, a = map(int, input().split())
  if a == 1:
    left = max(left, x)
  elif a == 2:
    right = min(right, x)
  elif a == 3:
    down = max(down, y)
  else:
    up = min(up, y)
    
w, h = 0, 0
if right-left > 0:
  w = right - left
if up-down > 0:
  h = up-down
ans = w * h
print(ans)