h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
dy=[1, 0, -1, 0]
dx=[0, 1, 0 ,-1]

from collections import deque
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            continue
        d=[[-1]*w for _ in range(h)]
        queue=deque()
        queue.append((i,j))
        d[i][j]=0
        tmp_ans=-1
        while queue:
            y,x=queue.popleft()
            for d_y, d_x in zip(dx,dy):
                new_y=y+d_y
                new_x=x+d_x
                if new_y<0 or h<=new_y or new_x<0 or w<=new_x:
                    continue
                if s[new_y][new_x]=='.' and d[new_y][new_x]==-1:
                    d[new_y][new_x]=d[y][x]+1
                    queue.append((new_y, new_x))
                    tmp_ans=max(tmp_ans, d[new_y][new_x])
        ans=max(ans, tmp_ans)
print(ans)
