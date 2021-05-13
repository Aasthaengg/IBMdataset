from collections import deque

h, w = [int(i) for i in input().split()]
a = [list(input()) for _ in range(h)]

b = [[-1 for _ in range(w)] for _ in range(h)]

q = deque()

for i in range(h):
    for j in range(w):
        if(a[i][j] == "#"):
            b[i][j] = 0
            q.append(i)
            q.append(j)
kotae = 0
while(len(q)):
    x = int(q.popleft())
    y = int(q.popleft())
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        if(0 <= x + dx[i] and x + dx[i] < h and 0 <= y + dy[i] and y + dy[i] < w):
            if(b[x+dx[i]][y+dy[i]] == -1):
                q.append(x + dx[i])
                q.append(y + dy[i])
                b[x+dx[i]][y+dy[i]] = b[x][y] + 1
                kotae = max(kotae, b[x+dx[i]][y+dy[i]])
print(kotae)




