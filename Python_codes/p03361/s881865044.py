h,w=map(int,input().split())
s=[input() for _ in range(h)]
d=[[0,1],[1,0],[-1,0],[0,-1]]
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            continue
        ok=False
        for dx,dy in d:
            nx,ny=i+dx,j+dy
            if 0<=nx<h and 0<=ny<w:
                if s[nx][ny]=="#":
                    ok=True
        if not ok:
            print("No")
            exit()
print("Yes")