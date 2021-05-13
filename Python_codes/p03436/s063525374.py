from collections import deque
h, w = map(int, input().split())
s = [input() for _ in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
table = [[float('inf') for _ in range(w)] for _ in range(h)]
table[0][0] = 0
def bfs():
    que = deque([[0, 0]])
    # print(que)
    used = [[0 for _ in range(w)] for _ in range(h)]
    used[0][0] = 1
    while que:
        # print(que.popleft())
        y, x = que.popleft()
        for k in range(4):
            if 0 <= y+dy[k] < h and 0 <= x+dx[k] < w:
                if s[y+dy[k]][x+dx[k]] == '#':
                    continue
                if used[y+dy[k]][x+dx[k]] == 0:
                    table[y+dy[k]][x+dx[k]] = min(table[y+dy[k]][x+dx[k]], table[y][x]+1)
                    used[y+dy[k]][x+dx[k]] = 1
                    que.append((y+dy[k], x+dx[k]))
    
    # print(*table, sep='\n')
    return table[h-1][w-1]

c = bfs()
if c == float('inf'):
    print(-1)
else:
    white = 0
    for i in range(h):
        white += s[i].count('.')
    ans = white - (c+1)
    print(ans)
