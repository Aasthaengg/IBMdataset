from collections import deque

H, W = list(map(int,input().split()))
A = [input() for _ in range(H)]

from collections import deque

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]  

def bfs(q, a):
  
    ret = deque([])
    while(q):
        pop = q.popleft()
        x, y = pop[0], pop[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < W and ny >= 0 and ny < H:
                if a[ny][nx] == -1:
                    ret.append([nx, ny])
                    a[ny][nx] = 0
    return ret, a
  
q = deque([])

a = [[0 for _ in range(W)] for _ in range(H)]
for i in range(W):
    for j in range(H):
        if A[j][i] == ".":
            a[j][i] = -1  

ans = 0
for i in range(W):
    for j in range(H):
        if a[j][i] == 0:
            q.append([i, j])

ans = -1
while q:
    ans += 1
    q, a = bfs(q, a)
            
print(ans)