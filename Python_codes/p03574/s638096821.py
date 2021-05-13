H, W = map(int, input().split())
S = [input() for _ in range(H)]

def getBomb(x, y):
  if x < 0 or y < 0 or x >= W or y >= H:
    return 0
  if S[y][x] == "#":
    return  1
  return 0

def getBombNum(x, y):
  total = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        if getBomb(x, y) == 1:
          return -1
      else:
        total += getBomb(x + i, y + j)
  return total

table = [0] * (W * H)
for y in range(H):
  for x in range(W):
    num = getBombNum(x, y)
    if num < 0:
      print("#", end="")
    else:
      print(num, end="")
  print()
