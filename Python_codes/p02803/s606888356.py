import sys
from collections import deque
input = sys.stdin.readline

h,w=map(int,input().split())
M=[list(input().strip()) for _ in range(h)]

def bfs(x,y):
    if M[x][y]=='#':
        return 0
    q=deque()
    q.append((x,y))
    count = [[-1]*w for _ in range(h)]
    count[x][y]=0

    while q:
        x,y=q.pop()
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=i<h and 0<=j<w and count[i][j]==-1 and M[i][j]=='.':
                count[i][j]=count[x][y]+1
                q.appendleft((i,j))

    return max([max(c) for c in count])
        
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans,bfs(i,j))
print(ans)

 
