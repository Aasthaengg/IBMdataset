H, W = map(int, input().split())

visited = [[False]*(W+2) for _ in range(H+2)]
dh = [0,1,0,-1]
dw = [1,0,-1,0]

from collections import deque
d = deque()

S = [0]*(H+2)
S[0] = '*'*(W+2)
S[H+1] = '*'*(W+2)
white = 0
for h in range(1,H+1):
    S[h] = '*' + input() + '*'
    for w in range(1,W+1):
        if S[h][w]=='#':
            visited[h][w]=True
            d.append((h,w,0))
    


while len(d)>0:
    h,w,cnt = d.popleft()
    for i in range(4):
        h0 = h+dh[i]
        w0 = w+dw[i]
        if S[h0][w0]=='.' and visited[h0][w0]==False:
            visited[h0][w0]=True
            d.append((h0,w0,cnt+1))
print(cnt)