from collections import deque
def main():
    h,w = map(int,input().split())
    grid = []
    dq = deque([])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    ans = 0
    d = [[-1 for i in range(w)] for j in range(h)]
    for i in range(h):
        maze = list(input())
        for j in range(w):
            if maze[j] == "#":
                dq.append((j,i))
                d[i][j] = 0
        grid.append(maze)
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= w-1 and 0 <= ny <= h-1 and grid[ny][nx] != "#" and d[ny][nx] == -1:
                dq.append((nx,ny))
                d[ny][nx] = d[y][x] + 1
                ans = max(ans,d[ny][nx])
    print(ans)
main()