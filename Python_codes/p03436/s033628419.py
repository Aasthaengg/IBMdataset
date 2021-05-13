h,w=map(int,input().split())
maze=[list(input()) for _ in range(h)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
queue=[]
ans = 0
cn = 0
for i in maze:
     cn += i.count("#")
queue.append([0,0,0])
while len(queue)>0:
    x,y,cnt=queue.pop(0)
    ans=cnt
    if x == h - 1 and y == w - 1:
        print(h*w-ans-cn-1)
        exit()
    for i in range(4):
        X=x+dx[i]
        Y = y + dy[i]
        if not (0 <= X < h and 0 <= Y < w):
             continue
        if maze[X][Y]=="#":
            continue
        if maze[X][Y]==".":
            queue.append([X,Y,cnt+1])
            maze[X][Y]="#"
print(-1)
