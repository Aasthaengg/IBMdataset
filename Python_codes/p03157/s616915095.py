from collections import deque
h,w=map(int,input().split())
field=[["*" for i in range(w+2)]]+[["*"]+list(input())+["*"] for i in range(h)]+[["*"]*(w+2)]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
visited=[[False for i in range(w+2)] for j in range(h+2)]
s={"#":0,".":1}
ans=0
def bfs(a,b):
    if visited[a][b] or field[a][b]=="*":return 0
    D=deque([(a,b)])
    visited[a][b]=True
    cnt=[0,0]
    while D:
        pos=D.popleft()
        cnt[s[field[pos[0]][pos[1]]]]+=1
        for i,j in zip(dx,dy):
            if field[pos[0]+i][pos[1]+j] == "*" or visited[pos[0]+i][pos[1]+j] or field[pos[0]+i][pos[1]+j]==field[pos[0]][pos[1]]:
                continue
            visited[pos[0]+i][pos[1]+j]=True
            D.append((pos[0]+i,pos[1]+j))
    return cnt[0]*cnt[1]
for i in range(h+2):
    for j in range(w+2):
        ans += bfs(i,j)
print(ans)