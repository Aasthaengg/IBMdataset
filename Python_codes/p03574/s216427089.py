import itertools
H,W = map(int,input().split())
S = [input() for h in range(H)]
a = [[0 if cell=="." else "#" for cell in row] for row in S]

for h in range(H):
  for w in range(W):
    if S[h][w]!="#":
      continue
    for dx,dy in itertools.product([-1,0,1],repeat=2):
      x = h+dx
      y = w+dy
      if x<0 or H<=x:
        continue
      if y<0 or W<=y:
        continue
      if S[x][y]=="#":
        continue
      a[x][y]+=1

for row in a:
  print(*row,sep="")