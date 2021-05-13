H, W = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(10)]

for k in range(10):
  for i in range(10):
    for j in range(10):
      mp[i][j] = min(mp[i][j], mp[i][k]+mp[k][j])
    
rlt = 0
for i in range(H):
  for j in map(int, input().split()):
    if j != -1 and j != 1:
      rlt += mp[j][1]
      
print(rlt)