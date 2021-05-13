from collections import deque
h,w = map(int,input().split())
m = ["#"*(w+2)]+["#"+input()+"#" for i in range(h)]+["#"*(w+2)]
temp = [[-1]*(w+2) for i in range(h+2)]
opt = [(1,0),(0,1),(-1,0),(0,-1)]
dq = deque()
ans = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        if m[i][j] == "#":
            dq.append((i,j))
            temp[i][j] = 0
while dq:
    y,x = dq.popleft()
    for i in opt:
        y1 = y+i[0]
        x1 = x+i[1]
        if m[y1][x1] == "." and temp[y1][x1] == -1:
            temp[y1][x1] = temp[y][x]+1
            ans = max(ans,temp[y1][x1])
            dq.append((y1,x1))
print(ans)