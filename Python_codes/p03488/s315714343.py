s=input()+'T'
x,y=list(map(int,input().split()))
x+=8000
y+=8000
n=len(s)
i=0

while i<n and s[i]=='F':
    i+=1

dx=[[0]*16001 for _ in range(2)]
dy=[[0]*16001 for _ in range(2)]

dx[0][i+8000]=1
dy[0][8000]=1

lstx=[]
lsty=[]
d='x'
cnt=0

while i<n:
    if s[i]=='F':
        cnt+=1
    else:
        if cnt>0:
            if d=='x':
                lstx.append(cnt)
            else:
                lsty.append(cnt)
        
        if d=='x':
            d='y'
        else:
            d='x'
        cnt=0
    
    i+=1

for i,cx in enumerate(lstx):
    for j in range(16001):
        if dx[i%2][j]==0:
            continue
        if j+cx<16001:
            dx[(i+1)%2][j+cx]=1
        if j-cx>-1:
            dx[(i+1)%2][j-cx]=1
    dx[i%2]=[0]*16001

for i,cy in enumerate(lsty):
    for j in range(16001):
        if dy[i%2][j]==0:
            continue
        if j+cy<16001:
            dy[(i+1)%2][j+cy]=1
        if j-cy>-1:
            dy[(i+1)%2][j-cy]=1
    dy[i%2]=[0]*16001

if dx[(len(lstx))%2][x]==1 and dy[(len(lsty))%2][y]==1:
    print('Yes')
else:
    print('No')