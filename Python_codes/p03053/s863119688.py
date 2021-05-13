h,w = map(int,input().split())
a = [input() for i in range(h)]

from collections import deque
q = deque()
reach = [[False]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j]=='#':
            q.append([i,j,0])
            reach[i][j] = True

ans = 0
while q:
    i,j,cnt = q.popleft()
    ans = max(ans,cnt)
    for k,l in [[1,0],[-1,0],[0,1],[0,-1]]:
        if 0<=i+k<h and 0<=j+l<w:
            if not reach[i+k][j+l]:
                q.append([i+k,j+l,cnt+1])
                reach[i+k][j+l] = True

print(ans)