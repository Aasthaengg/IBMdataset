sx,sy,tx,ty = map(int, input().split())

rlt = []
for _ in range(tx-sx):
  rlt.append('R')
for _ in range(ty-sy):
  rlt.append('U')
for _ in range(tx-sx):
  rlt.append('L')
for _ in range(ty-sy+1):
  rlt.append('D')
for _ in range(tx-sx+1):
  rlt.append('R')
for _ in range(ty-sy+1):
  rlt.append('U')
rlt.append('L')
rlt.append('U')
for _ in range(tx-sx+1):
  rlt.append('L')
for _ in range(ty-sy+1):
  rlt.append('D')
rlt.append('R')
  
print(''.join(rlt))