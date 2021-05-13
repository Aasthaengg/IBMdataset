from collections import deque
h,w = map(int,input().split())
sq = [list(input()) for i in range(h)]
prt = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
  for j in range(w):
    c = i + j
    if sq[i][j] == "#":
      c += 1
    prt[i][j] = c%2
que = deque([])
ans = 0
visited = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
  for j in range(w):
    if visited[i][j] != 1:
      que.append((i,j))
      cnt = 0
      cntb = 0
      while que:
        x,y = que.popleft()
        if visited[x][y] != 1:
          cnt += 1
          if sq[x][y] == "#":
            cntb += 1
          visited[x][y] = 1
          for n_x,n_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=n_x<h and 0<=n_y<w:
              if visited[n_x][n_y] != 1 and prt[n_x][n_y] == prt[x][y]:
                que.append((n_x,n_y))
      ans += cntb*(cnt-cntb)

print(ans)
