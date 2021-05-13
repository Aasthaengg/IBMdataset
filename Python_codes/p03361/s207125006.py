H, W = map(int, input().split())
s = [list(input()) for i in range(H)]

fail = 0

for i in range(H):
  for j in range(W):
    if i == 0:
      if j == 0:
        if s[i][j] == '.':
          pass
        elif s[i][min(W-1,j+1)] == '#' or s[min(H-1,i+1)][j] == '#':
          pass
        else:
          fail += 1
      elif j == W - 1:
        if s[i][j] == '.':
          pass
        elif s[i][max(0,j-1)] == '#' or s[min(H-1,i+1)][j] == '#':
          pass
        else:
          fail += 1
      else:
        if s[i][j] == '.':
          pass
        elif s[i][j-1] == '#' or s[i][j+1] == '#' or s[min(H-1,i+1)][j] == '#':
          pass
        else:
          fail += 1
    elif i == H - 1:
      if j == 0:
        if s[i][j] == '.':
          pass
        elif s[i][min(W-1,j+1)] == '#' or s[max(0,i-1)][j] == '#':
          pass
        else:
          fail += 1
      elif j == W - 1:
        if s[i][j] == '.':
          pass
        elif s[i][max(0,j-1)] == '#' or s[max(0,i-1)][j] == '#':
          pass
        else:
          fail += 1
      else:
        if s[i][j] == '.':
          pass
        elif s[i][j-1] == '#' or s[i][j+1] == '#' or s[max(0,i-1)][j] == '#':
          pass
        else:
          fail += 1
    else:
      if j == 0:
        if s[i][j] == '.':
          pass
        elif s[i-1][j] == '#' or s[i+1][j] == '#' or s[i][min(H-1,j+1)] == '#':
          pass
        else:
          fail += 1
      elif j == W - 1:
        if s[i][j] == '.':
          pass
        elif s[i-1][j] == '#' or s[i+1][j] == '#' or s[i][max(0,j-1)] == '#':
          pass
        else:
          fail += 1
      else:
        if s[i][j] == '.':
          pass
        elif s[i-1][j] == '#' or s[i+1][j] == '#' or s[i][j-1] == '#' or s[i][j+1] == '#':
          pass
        else:
          fail += 1
          
isAllWhite = False
count = 0
for i in range(H):
  for j in range(W):
    if s[i][j] == '.':
      count += 1
else:
  if count == H * W:
    isAllWhite = True
    
  if isAllWhite or fail == 0:
    print('Yes')
  else:
    print('No')