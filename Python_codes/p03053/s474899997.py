from collections import deque

H,W = map(int,input().split())

S = [None]*W
S = [list(input()) for i in range(H)]
light = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            light.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

not_visited = [[-1]*W for i in range(H)]
stack = deque()
for k in range(len(light)):
    stack.append(light[k])
    i,j = light[k]
    not_visited[i][j] = 0

while stack != deque([]):
    y,x = stack.popleft()
    for i in range(4):
        if 0<= x+dx[i] <W and 0<= y+dy[i] <H and not_visited[y+dy[i]][x+dx[i]] == -1:
            not_visited[y+dy[i]][x+dx[i]] =  not_visited[y][x] + 1
            stack.append((y+dy[i],x+dx[i]))

ans = -1
for i in range(H):
    ans = max(ans,max(not_visited[i]))

print(ans)