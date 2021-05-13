from collections import deque

N,M = map(int,input().split())
ad = [[[] for _ in range(3)] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    for j in range(3):
        ad[u][j].append((v,(j+1)%3))
S,T = map(int,input().split())
S -= 1
T -= 1

visited = [[False]*3 for _ in range(N)]
dq = deque()
dq.append((S,0,0))
visited[S][0] = True

while dq:
    v,j,d = dq.popleft()
    nd = d + 1
    for nv,nj in ad[v][j]:
        if (nv,nj) == (T,0):
            print(nd//3)
            exit()
        if visited[nv][nj]:
            continue
        visited[nv][nj] = True
        dq.append((nv,nj,nd))
        
print(-1)