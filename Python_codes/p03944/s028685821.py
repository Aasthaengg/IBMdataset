w, h, n = map(int, input().split())

white = [0, w, 0, h]

for i in range(n):
  x, y, a = map(int, input().split())
  if a == 1:
    white[0] = max(x, white[0])
  elif a == 2:
    white[1] = min(x, white[1])
  elif a == 3:
    white[2] = max(y, white[2])
  elif a == 4:
    white[3] = min(y, white[3])
if white[1] - white[0] <= 0 or white[3] - white[2] <= 0:
  print(0)
else:
  print((white[1] - white[0]) * (white[3] - white[2]))