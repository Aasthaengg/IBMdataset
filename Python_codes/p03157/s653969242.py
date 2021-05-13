from collections import deque

h, w = map(int, input().split())
S = []
for _ in range(h):
    s = str(input())
    S.append(s)

dq = deque([])
if S[0][0] == '.':
    dq.append([0,0,'.'])
else:
    dq.append([0,0,'#'])

Visited = [[False for _ in range(w)] for _ in range(h)]
Visited[0][0] = True

All_grid = deque([])
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            pass
        else:
            All_grid.append([i,j])

ans = 0
black = 0
white = 0
while dq:
    now = dq.popleft()

    y = now[0]
    x = now[1]
    color = now[2]

    if color == '.':
        white += 1
    else:
        black += 1

    Nexts = [[y,x-1], [y,x+1], [y-1,x], [y+1,x]]
    for nex in Nexts:
        if nex[0] >= h or nex[0] < 0 or nex[1] >= w or nex[1] < 0:
            continue
        if Visited[nex[0]][nex[1]] == True:
            continue

        if color == '.' and S[nex[0]][nex[1]] == '.':
            continue
        elif color == '#' and S[nex[0]][nex[1]] == '#':
            continue
        elif color == '.' and S[nex[0]][nex[1]] == '#':
            dq.append([nex[0], nex[1], '#'])
            Visited[nex[0]][nex[1]] = True
        else:
            dq.append([nex[0], nex[1], '.'])
            Visited[nex[0]][nex[1]] = True

    if len(dq) == 0:
        ans += black * white
        black = 0
        white = 0

        while All_grid:
            cand = All_grid.popleft()
            i = cand[0]
            j = cand[1]
            if Visited[i][j] == False:
                c = S[i][j]
                dq.append([i,j,c])
                Visited[i][j] = True
                break

print(ans)