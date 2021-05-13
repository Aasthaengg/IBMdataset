from collections import deque
h,w=map(int,input().split())
l=['@'*(w+2)]
for i in range(h):
    l.append('@'+input()+'@')
l.append('@'*(w+2))
s=[[-1 for i in j] for j in l]
s[1][1]=l[1][1]=='#'
q=deque([[1,1]])
while len(q)>0:
    x,y=q.popleft()
    for i,j in [[1,0],[0,1]]:
        if l[i+x][j+y]!='@' and s[i+x][j+y]==-1:
            if l[x][y]==l[i+x][j+y]:
                q.appendleft([i+x,j+y])
                s[i+x][j+y]=s[x][y]
            else:
                q.append([i+x,j+y])
                s[i+x][j+y]=s[x][y]+1
print(-s[h][w]//2*-1)
#print(*l,*s,sep='\n')