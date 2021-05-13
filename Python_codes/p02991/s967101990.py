from collections import deque
N,M = map(int,input().split())
dis = [[-1,-1,-1] for _ in range(N+1)]
Tree = [[] for _ in range(N+1)]
for i in range(M):
    ui,vi = map(int,input().split())
    Tree[ui].append(vi)
S,T = map(int,input().split())
d = deque([(S,0)])
dis[S][0] = 0
while d:
    x,z = d.popleft()
    for y in Tree[x]:
        if dis[y][(z+1)%3] == -1:
            dis[y][(z+1)%3] = dis[x][z] + 1
            d.append((y,(z+1)%3))
if dis[T][0] == -1:
    print(-1)
else:
    print(dis[T][0]//3)