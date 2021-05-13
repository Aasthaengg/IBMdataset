dy = (-1,0,1,0)
dx = (0,1,0,-1)
from collections import deque

def main():
    h,w = map(int,input().split())
    grid = [input() for _ in range(h)]
    q = deque([])
    dist = [[-1] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                dist[i][j] = 0
                q.append((i,j))
    
    ans = 0
    while q:
        i,j = q.popleft()
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if y < 0 or y >= h:
                continue
            if x < 0 or x >= w:
                continue
            if dist[y][x] < 0:
                dist[y][x] = dist[i][j] + 1
                ans = max(ans,dist[y][x])
                q.append((y,x))
    print(ans)
if __name__ == '__main__':
    main()
