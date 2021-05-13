h,w=map(int,input().split())
grid =[list(input()) for i in range(h)]
visited=[[False]*w for i in range(h)]
ans=0
for i in range(h):
  for j in range(w):
    if visited[i][j]:
      continue
    q=[(i,j)]
    d={'#':0,'.':0}
    while q:
      cy,cx=q.pop(0)
      for ny,nx in ((cy+1,cx),(cy-1,cx),(cy,cx+1),(cy,cx-1)):
        if not(0<=ny<h and 0<=nx<w) or grid[cy][cx]==grid[ny][nx] or visited[ny][nx]:
          continue
        d[grid[ny][nx]]+=1
        visited[ny][nx]=True
        q.append((ny,nx))
    ans+=d['.']*d['#']
print(ans)