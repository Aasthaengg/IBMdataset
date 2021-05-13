import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

h,w = list(map(int, input().split()))
s = [None]*h
for i in range(h):
    s[i] = input()
start = (0,0)
# 高さh, 幅w
from queue import deque
vals = [None] * (w*h)
q = deque([(0, start)]) # (距離, ノード番号)
vals[start[0]*w+start[1]] = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
while q:
    val, (x,y) = q.popleft()
    for i, j in zip(dx,dy):
        xx, yy = x+i, y+j
        if xx<0 or xx>=h or yy<0 or yy>=w or s[xx][yy]=="#":
            continue
        if vals[xx*w+yy] is None:
            vals[xx*w+yy] = val+1
            q.append((vals[xx*w+yy], (xx,yy)))

dist = vals[-1]
if dist is None:
    ans = -1
else:
    ans = (h*w) - (dist+1) - sum(sum(item=="#" for item in ss) for ss in s)
print(ans)