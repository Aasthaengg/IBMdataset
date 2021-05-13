from collections import deque
H, W = map(int, input().split())
area = [['#']*(W+2)]
space = 0
for i in range(H):
    temp = ['#']+list(input())+['#']
    for t in temp:
        if t=='.': space+=1 
    area.append(temp)
area.append(['#']*(W+2))
move = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
dq = deque([(1,1)])
dist = [[-1]*(W+2) for _ in range(H+2)]
dist[1][1] = 1
    
while dq:
    nowx, nowy = dq.popleft()
    if (nowx, nowy) == (W, H): break
    for dx, dy in move:
        nxtx, nxty = nowx+dx, nowy+dy
        if not 0<=nxtx<W+2 and 0<=nxty<H+2: continue
        if dist[nxty][nxtx]>=0 or area[nxty][nxtx]=='#': continue
        dist[nxty][nxtx] = dist[nowy][nowx]+1
        dq.append((nxtx, nxty))
if dist[H][W]==-1: print(-1)
else: print(space-dist[H][W])