H, W  = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(H)]


ans = 0
ansgrid = []


for i in range(H):
  for j in range(W):
    if grid[i][j] % 2 == 1:
      if i == H-1:
        if j != W-1:
          ansgrid.append([i,j,i,j+1])
          ans += 1
          grid[i][j] -= 1
          grid[i][j+1] += 1
        else:
          break


      
      else:
        ansgrid.append([i,j,i+1,j])
        ans += 1
        grid[i][j] -= 1
        grid[i+1][j] += 1

        


print(ans)
for i in range(len(ansgrid)):
  print(ansgrid[i][0]+1,ansgrid[i][1]+1,ansgrid[i][2]+1,ansgrid[i][3]+1)