from collections import deque

H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

#右上左下
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


ans = 0

que = deque()

num_white = H * W

paint = 0

for i in range(H):
    for j in range(W):
        if field[i][j] == "#":
            que.append((i, j))
            num_white -= 1

def check(field):
    flag = False
    for i in range(H):
        if "." in field[i]:
            flag = True

    return flag

def one_bsf():
    global paint
    global que
    global ans

    for _ in range(len(que)):
        n = que.popleft()
        ny = n[0]
        nx = n[1]

        for i in range(4):
            nny = ny + dy[i]
            nnx = nx + dx[i]

            if nny < 0 or nny >= H or nnx < 0 or nnx >= W:
                continue

            elif field[nny][nnx] == ".":
                field[nny][nnx] = "#"
                paint += 1
                que.append((nny, nnx))

    ans += 1

while num_white != paint:
    one_bsf()
    
print(ans)