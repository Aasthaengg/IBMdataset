from collections import deque
H,W=map(int,input().split())
arr=[list(map(str,input())) for i in range(H)]

vist=[[0]*W  for i in range(H)]
dxdy=[[-1,0],[1,0],[0,-1],[0,1]]

d=deque([[0,0,1]])


ans=0

while len(d)>0:
    a=d.popleft()
    x,y,z=a[0],a[1],a[2]

    if x==H-1 and y==W-1:
        ans=z
        break
    
    elif arr[x][y]=="." and vist[x][y]==0:
        vist[x][y]=1
        for dx,dy in dxdy:
            if (0<=x+dx<H) and (0<=y+dy<W):
                if arr[x+dx][y+dy]==".":
                    d.append([x+dx,y+dy,z+1])

count=0
for i in range(H):
    for j in range(W):
        if arr[i][j]=="#":
            count+=1
if ans==0:
    print(-1)
else:
    print(H*W-count-ans)