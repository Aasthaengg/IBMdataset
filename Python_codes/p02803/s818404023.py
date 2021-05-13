from collections import deque

h,w = map(int, input().split())
grid = []
for i in range(h):
    s = list(input().rstrip())
    grid.append(s)
dydx = [[0, 1], [1,0], [-1, 0], [0, -1]]

def find_longest_path(xy):
    visited = [[0]*w for _ in range(h)]
    dist = [[0]*w for _ in range(h)]
    visited[xy[1]][xy[0]]=1
    que = deque()
    que.append(xy)
    while que:
        v = que.popleft()
        x,y = v[0],v[1]
        for i in dydx:
            dx = i[0]
            dy = i[1]
            if ((x+dx<w and y+dy<h) and ((x+dx)>-1)and(y+dy)>-1) and not visited[y+dy][x+dx]:
                if(grid[y+dy][x+dx]=="."):
                    que.append([x+dx, y+dy])
                    visited[y+dy][x+dx]=1
                    dist[y+dy][x+dx]=dist[y][x]+1
                    u,k = x+dx, y+dy
                    r = dist[y+dy][x+dx]

    return r

def main():
    k=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==".":
                k = max(k, find_longest_path([j,i]))
    print(k)

if __name__ == '__main__':
    main()
