from collections import deque
H, W = map(int, input().split())
S = [input() for _ in range(H)]

dist = [[-1]*W for _ in range(H)]
dist[0][0]=1
d=deque()
d.append((0,0))

while d:
    pop = d.popleft()
    y, x = pop[0], pop[1]

    y_lst = [y+1, y-1, y, y]
    x_lst = [x, x, x+1, x-1]

    for Y, X in zip(y_lst, x_lst):
        if not (0 <= Y < H) or not (0 <= X < W) or S[Y][X]=="#":
            continue
        if dist[Y][X]==-1:
            dist[Y][X] = dist[y][x] + 1
            d.append((Y, X))

if dist[H-1][W-1]==-1:
    print(-1)
else:
    goaltime = dist[H-1][W-1]
    white_sum = 0
    for i in S:
        white_sum += i.count(".")
    print(white_sum-goaltime)
