from collections import deque
H,W=map(int,input().split())

q=deque()
dist=[[-1]*(W+1) for a in range(H+1)]
G=[['#']*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    G_comp=list(str(input()))
    for j in range(1,W+1):
        if G_comp[j-1]=='#':
            q.append((i,j))
            dist[i][j]=0
        G[i][j]=G_comp[j-1]

def sur(v):  #v is tuple
    vx=v[0]
    vy=v[1]
    preE=[(vx-1,vy),(vx+1,vy),(vx,vy-1),(vx,vy+1)]
    E=[]
    for nv in preE:
        if 1<=nv[0]<=H and 1<=nv[1]<=W:
            if G[nv[0]][nv[1]]=='.':
                E.append(nv)
    return E

while q:
    now=q.popleft()
    for next in sur(now):
        if dist[next[0]][next[1]]!=-1:
            continue
        q.append(next)
        dist[next[0]][next[1]]=dist[now[0]][now[1]]+1

M=[]
for k in range(1,H+1):
    M.append(max(dist[k]))

print(max(M))




