import sys
sys.setrecursionlimit(10**8)
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

es = [[[] for j in range(i)] for i in range(N)]
indeg = [[0]*i for i in range(N)]
for i,row in enumerate(A):
    for x,y in zip(row,row[1:]):
        x,y = x-1,y-1
        a0,b0 = (i,x) if i>x else (x,i)
        a1,b1 = (i,y) if i>y else (y,i)
        es[a0][b0].append((a1,b1))
        indeg[a1][b1] += 1

status = [[-1]*i for i in range(N)] #-1:new 0:active 1:finished
def has_cycle(v):
    a0,b0 = v
    status[a0][b0] = 0
    for a1,b1 in es[a0][b0]:
        if status[a1][b1] == 0: return True
        if status[a1][b1] == -1:
            if has_cycle((a1,b1)): return True
    status[a0][b0] = 1
    return False

for i in range(N):
    for j in range(i):
        if status[i][j] != -1: continue
        if has_cycle((i,j)):
            print(-1)
            exit()

from collections import deque
q = deque()
for i in range(N):
    for j in range(i):
        if indeg[i][j] == 0:
            q.append((i,j,1))

ans = -1
while q:
    a0,b0,d = q.popleft()
    ans = max(ans,d)
    for a1,b1 in es[a0][b0]:
        indeg[a1][b1] -= 1
        if indeg[a1][b1] == 0:
            q.append((a1,b1,d+1))
print(ans)