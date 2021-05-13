from collections import deque

H, W = map(int, input().split())

mp = ['#'*(W+1)]
memo = [[-1]*(W+1) for _ in range(H+1)]

cnt = 0
for _ in range(H):
  s = '#'+input()
  cnt += s.count('.')
  mp.append(s)
  
ds = [[1,0], [-1,0], [0,1], [0,-1]]
h = deque([[1,1,1]])
while h:
  l = h.popleft()
  for d in ds:
    if l[0]+d[0] <= W and l[1]+d[1] <= H:
      if mp[l[1]+d[1]][l[0]+d[0]] == '.' and memo[l[1]+d[1]][l[0]+d[0]] == -1:
        memo[l[1]+d[1]][l[0]+d[0]] = l[2] + 1
        h.append([l[0]+d[0], l[1]+d[1], l[2] + 1])
  if memo[H][W] > -1:
    print(cnt-memo[H][W])
    exit()
    
print(memo[H][W])