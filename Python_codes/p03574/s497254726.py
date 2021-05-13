h,w = map(int,input().split())
s = [list(input()) for i in range(h)]

def count_mine(i, j, s, h, w):
  mine = 0
  # 一段上
  if i-1 >= 0 and j-1 >= 0 and s[i-1][j-1] == "#":
    mine += 1
  if i-1 >= 0 and s[i-1][j] == "#":
    mine += 1
  if i-1 >= 0 and j+1 < w and s[i-1][j+1] == "#":
    mine += 1
  
  # 真ん中
  if j-1 >= 0 and s[i][j-1] == "#":
    mine += 1
  if j+1 < w and s[i][j+1] == "#":
    mine += 1
    
  # 一段下
  if i+1 < h and j-1 >= 0 and s[i+1][j-1] == "#":
    mine += 1
  if i+1 < h and s[i+1][j] == "#":
    mine += 1
  if i+1 < h and j+1 < w and s[i+1][j+1] == "#":
    mine += 1
    
  return mine

for i in range(h):
  for j in range(w):
    if s[i][j] == ".":
      s[i][j] = count_mine(i, j, s, h, w)
  print(''.join(map(str, s[i])))
  

