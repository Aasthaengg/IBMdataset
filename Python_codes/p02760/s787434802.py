a = []
b = []
for _ in range(3):
  a.append(list(map(int,input().split())))
n = int(input())
for _ in range(n):
  b.append(int(input()))

for i in range(n):
  for j in range(3):
    for k in range(3):
      if a[j][k] == b[i]:
        a[j][k] = 0
        
flg = 0
if flg == 0:
  for i in range(3):
    if flg ==0:
      for j in range(3):
        if a[i][j] == 0 and j != 2:
          continue
        elif j == 2 and a[i][j]==0:
          flg = 1
        else:
          break
if flg == 0:
  for i in range(3):
    if flg ==0:
      for j in range(3):
        if a[j][i] == 0 and j != 2:
          continue
        elif j == 2 and a[j][i]==0:
          flg = 1
        else:
          break
if flg == 0:
  for i in range(3):
    if a[i][i] == 0 and i != 2:
      continue
    elif a[i][i] == 0:
      flg = 1
    else:
      break
if flg == 0:
  for i in range(3):
    if a[i][2-i] == 0 and i != 2:
      continue
    elif a[i][2-i] == 0:
      flg = 1
    else:
      break
if flg == 0:
  print("No")
else:
  print("Yes")