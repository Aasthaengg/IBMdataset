from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
flag = [[-1 for _ in range(W)] for _ in range(H)]

now = 0
for i in range(H):
    for j in range(W):
        if flag[i][j] == -1:
            stack = deque([]) 
            stack.append([i, j])
            flag[i][j] = now
            while len(stack) > 0:
                y, x = stack.popleft()
                for nx, ny in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                    if 0<= x + nx < W and 0 <= y + ny < H:
                        if S[y][x] != S[y+ny][x+nx] and flag[y+ny][x+nx] == -1:
                            stack.append([y+ny, x+nx])
                            flag[y+ny][x+nx] = now
            now += 1
    
Black = [0 for _ in range(now+1)]
White = [0 for _ in range(now+1)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            Black[flag[i][j]] += 1
        else:
            White[flag[i][j]] += 1
   
res = 0
for i in range(now + 1):
    res += Black[i] * White[i]
    
print(res)