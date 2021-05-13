h,w = map(int,input().split())
grid = []
for i in range(h):
  grid.append(input())
walk = [[1,0],[-1,0],[0,1],[0,-1]]
ans = 'Yes'
for i in range(h):
  for j in range(w):
    if grid[i][j]=='#':
      temp = 1
      for k,l in walk:
        ni = i+k
        nj = j+l
        if 0<=ni<h and 0<=nj<w:
          if grid[ni][nj]=='#':
            temp = 0
      if temp:
        ans = 'No'
print(ans)