H, W, K = map(int, input().split())

mp = [input() for _ in range(H)]

memo = [[0]*W for _ in range(H)]

cnt = 0
for i in range(H):
  if '#' in mp[i]:
    cnt += 1
    tmp = 0
    for j in range(W):
      if mp[i][j] == '#':
        if tmp > 0:
          cnt += 1
        tmp += 1
      memo[i][j] = cnt
  else:
    if i > 0:
      memo[i] = memo[i-1]
      
nz = 0
for i in range(H):
  if memo[i][0] > 0:
    nz = i
    break
    
if nz > 0:
  for i in range(nz, 0, -1):
    memo[i-1] = memo[i]
  
for i in range(H):
  print(" ".join(map(str, memo[i])))