t,*grid=open(0)
h,w=map(int,t.split())
vis=[[False]*w for _ in range(h)]
ans=0
for y in range(h):
	for x in range(w):
		if vis[y][x]:
			continue
		q=[(y,x)]
		d={"#":0,".":0}
		while q:
			cy,cx=q.pop(0)
			for ny,nx in ((cy+1,cx),(cy-1,cx),(cy,cx+1),(cy,cx-1)):
				if not (0<=ny<h and 0<=nx<w) or vis[ny][nx] or grid[cy][cx]==grid[ny][nx]:
					continue
				d[grid[ny][nx]]+=1
				vis[ny][nx]=True
				q.append((ny,nx))
		ans+=d["#"]*d["."]
print(ans)
