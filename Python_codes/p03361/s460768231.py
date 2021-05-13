h,w=map(int,input().split())
g=[list(input()) for _ in range(h)]
for x in range(h):
    for y in range(w):
        if g[x][y]=="#":
            k=0
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx=x+i
                ny=y+j
                if nx<0 or nx>=h or ny<0 or ny>=w:
                   continue
                if g[nx][ny]==".":
                    k+=1
            if k==4:
                print("No")
                exit()
print("Yes")