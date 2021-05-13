from collections import deque
h,w = map(int, input().split())

m = [list(input()) for _ in range(h)]

def get_start_points(m):
    start_points = []
    for y in range(h):
        for x in range(w):
            if m[y][x] == '#':
                start_points.append((y,x))
    return start_points

def bfs(start_points):
    que = deque(start_points)
    step = 0
    count_flag = False
    while len(que):
        for q in range(len(que)):
            y,x = que.popleft()
            for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                ny = y + dy
                nx = x + dx
                if not (0<=ny<h and 0<=nx<w) or m[ny][nx] != '.':
                    continue
                m[ny][nx] = '#'
                count_flag = True
                que.append((ny,nx))

        if count_flag:
            step += 1
            count_flag = False
        else:
            break
    return step

print(bfs(get_start_points(m)))