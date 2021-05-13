H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
c = [[0]*W for _ in range(H)]

y, x = 0, 0
direction = 1
for i in range(N):
  for _ in range(a[i]):
    c[y][x] = (i+1)
    if direction == 1:
      if x+1 <= W-1:
        x += 1
      else:
        y += 1
        direction *= -1
    else:
      if x-1 >= 0:
        x -= 1
      else:
        y += 1
        direction *= -1
  
for cc in c:
  print(*cc)