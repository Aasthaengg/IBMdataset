n = int(input())
a = list(map(int, input().split()))
color = [0] * 8
cnt = 0
for i in a:
  if i < 400:
    color[0] = 1
  elif i < 800:
    color[1] = 1
  elif i < 1200:
    color[2] = 1
  elif i < 1600:
    color[3] = 1
  elif i < 2000:
    color[4] = 1
  elif i < 2400:
    color[5] = 1
  elif i < 2800:
    color[6] = 1
  elif i < 3200:
    color[7] = 1
  else:
    cnt += 1
if color.count(1) == 0:
  print(1, cnt)
else:
  print(color.count(1), color.count(1) + cnt)