from collections import deque

h,w=map(int,input().split())
G=[]
for i in range(h):
    G.append(list(str(input())))


#白マス数える
white=0
for i in range(h):
    for j in range(w):
        if G[i][j]=='.':
            white+=1


def sur(v):
    vx=v[0]
    vy=v[1]
    preE=[(vx-1,vy),(vx+1,vy),(vx,vy+1),(vx,vy-1)]
    E=[]
    for nv in preE:
        if 0<=nv[0]<=h-1 and 0<=nv[1]<=w-1:
            if G[nv[0]][nv[1]]=='.':
                E.append(nv)
    return E

#bfs
dist=[[0]*w for i in range(h)]
q=deque()

dist[0][0]=1
q.append((0,0))
while q:
    now=q.popleft()
    for next in sur(now):
        if dist[next[0]][next[1]]>0:
            continue
        q.append(next)
        dist[next[0]][next[1]]=dist[now[0]][now[1]]+1

        if next==(h-1,w-1):
            print(white-dist[h-1][w-1])
            break
    else:
        continue
    break
else:
    print(-1)




