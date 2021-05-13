h,w=map(int,input().split())
m=[]
for _ in range(h): m.append(list(input()))
black=0
white=0
for i in range(h):
    for j in range(w):
        if m[i][j]=="#": black+=1
white=h*w-black
node=[[0,0,1]]
dx,dy=[-1,0,1,0],[0,1,0,-1]
while node:
    temp=node.pop(0)
    if temp[0]==h-1 and temp[1]==w-1:
        print(h*w-black-temp[2])
        exit()
    m[temp[0]][temp[1]]="#"
    for i in range(4):
        if 0<=temp[0]+dx[i]<h and 0<=temp[1]+dy[i]<w:
            if m[temp[0]+dx[i]][temp[1]+dy[i]]==".":
                node.append([temp[0]+dx[i],temp[1]+dy[i],temp[2]+1])
                m[temp[0]+dx[i]][temp[1]+dy[i]]="#"
print(-1)           