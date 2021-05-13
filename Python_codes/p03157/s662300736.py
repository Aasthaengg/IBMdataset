
from collections import deque
h,w=map(int,input().split())
s=[]
for _ in range(h):
    s.append(input())
ans=0        
sc=[[0 for i in range(w)] for j in range(h)]

for x in range(h):
    for y in range(w):
        if s[x][y]=='.' or sc[x][y]==1:
            continue
        path = deque([[x,y]])
        sc[x][y]=1
        b=1
        wh=0
        while len(path)>0:
            p = path.popleft()
            i,j=p[0],p[1]
            tc = '.' if s[i][j] == '#' else '#'
            point = b if s[i][j] == '#' else wh           
            if i > 0 and s[i-1][j]==tc and sc[i-1][j]==0:
                sc[i-1][j]=1
                path.append([i-1,j])
                if s[i-1][j] == '#':
                    b += 1
                else:
                    wh += 1
                ans += point
            if j > 0 and s[i][j-1]==tc and sc[i][j-1]==0:
                sc[i][j-1]=1
                path.append([i,j-1])
                if s[i][j-1] == '#':
                    b += 1
                else:
                    wh += 1
                ans += point
            if i < h-1 and s[i+1][j]==tc and sc[i+1][j]==0:
                sc[i+1][j]=1
                path.append([i+1,j])
                if s[i+1][j] == '#':
                    b += 1
                else:
                    wh += 1
                ans += point
            if j < w-1 and s[i][j+1]==tc and sc[i][j+1]==0:
                sc[i][j+1]=1
                path.append([i,j+1])
                if s[i][j+1] == '#':
                    b += 1
                else:
                    wh += 1
                ans += point
print(ans)