from collections import deque
N,M = map(int,input().split())
node = [[10**9]*3 for i in range(N)]
KENPA = 3
side = [[]for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    side[u-1].append(v-1)
S,T = map(int,input().split())
node[S-1][2] = 0
queue = deque([[S-1,2]])
while queue:
    x,y = queue.popleft()
    y2 = (y+1)%KENPA
    for i in side[x]:
        if node[i][y2] > node[x][y]+1:
            node[i][y2] = node[x][y]+1
            queue.append([i,y2])
if node[T-1][2] == 10**9:
    print(-1)
else:
    print(node[T-1][2] // 3)
