from collections import deque

H, W = map(int,input().split())

mp = [input() for _ in range(H)]

rlt = 0
dxy = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(H):
  for j in range(W):
    if mp[i][j] == '#':
      continue
    memo = [[405]*W for _ in range(H)]
    memo[i][j] = 0
    q = deque([[i, j, 0]])
    tmp = 0
    while q:
      t = q.popleft()
      for d in dxy:
        if t[0]+d[0] >= 0 and t[0]+d[0] < H and t[1]+d[1] >= 0 and t[1]+d[1] < W:
          if mp[t[0]+d[0]][t[1]+d[1]] == '.' and memo[t[0]+d[0]][t[1]+d[1]] == 405:
            memo[t[0]+d[0]][t[1]+d[1]] = t[2] + 1
            q.append([t[0]+d[0], t[1]+d[1], t[2] + 1])
            tmp = max(tmp, t[2]+1)
    rlt = max(rlt, tmp)
    
print(rlt)