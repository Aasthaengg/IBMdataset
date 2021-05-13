from collections import deque
h,w = list(map(int,input().split()))
f = []
q = deque()
for i in range(h):
    a = list(input())
    for j in range(w):
        if a[j] == '#':
            q.append([0,i,j])
    f.append(a)
 
ans =0
dxy = [0,1,0,-1,0]
while(len(q)):
    c,y,x = q.popleft()
    for i in range(4):
        ny = y+dxy[i]
        nx = x+dxy[i+1]
        if nx >= w or ny >= h or nx <0 or ny <0:
            continue
        if f[ny][nx] == '.':
            f[ny][nx] = c+1
            q.append([c+1,ny,nx])
            ans = max(ans,c+1)
        elif f[ny][nx] != '#' and f[ny][nx] > c+1:
            f[ny][nx] = c+1
            q.append([c+1,ny,nx])
            ans = max(ans,c+1)
 
print(ans)