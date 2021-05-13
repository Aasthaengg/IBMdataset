H, W = map(int, input().split())

mp = []
for _ in range(H):
  mp.append(list(map(int, input().split())))

rlt = []
  
f = 0
for i in range(H):
  if i % 2 == 0:
    for j in range(W):
      if mp[i][j] % 2 == 1:
        f = (f + 1) % 2
      if f == 1:
        if j < W -1:
          rlt.append((i+1,j+1,i+1,j+2))
        else:
          rlt.append((i+1,j+1,i+2,j+1))
  else:
    for j in range(W-1,-1,-1):
      if mp[i][j] % 2 == 1:
        f = (f + 1) % 2
      if f == 1:
        if j > 0:
          rlt.append((i+1,j+1,i+1,j))
        else:
          rlt.append((i+1,j+1,i+2,j+1))
  
if f == 1:
  rlt.pop(-1)
  
print(len(rlt))
for t in rlt:
  print(" ".join(map(str, t)))