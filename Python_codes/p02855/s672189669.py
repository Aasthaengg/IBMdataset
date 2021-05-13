H,W,K,*L = open(0).read().split()
H,W,K = map(int, (H,W,K))
sheet = [[0]*W for i in range(H)]
cnt = 1
sep = [0]
n = 1
for i in range(H):
  for j in range(W):
    if L[i][j]=='#':
      sheet[i][j] = n
      n += 1      
for i in range(H):
  p = 0
  for j in range(W):
    if sheet[i][j]!=0:
      p = sheet[i][j]
    sheet[i][j] = p
for i in range(H):
  p = 0
  for j in range(W-1,-1,-1):
    if sheet[i][j]!=0:
      p = sheet[i][j]
    sheet[i][j] = p
for j in range(W):
  p = 0
  for i in range(H):
    if sheet[i][j]!=0:
      p = sheet[i][j]
    sheet[i][j] = p

for j in range(W):
  p = 0
  for i in range(H-1,-1,-1):
    if sheet[i][j]!=0:
      p = sheet[i][j]
    sheet[i][j] = p
for ans in sheet:
  print(' '.join(map(str,ans)))