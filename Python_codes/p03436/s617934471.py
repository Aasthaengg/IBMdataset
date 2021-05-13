import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
from collections import deque
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W = map(int, readline().split())
    maze = read().split('\n')

    d = [(1,0), (-1,0), (0,1), (0,-1)]
    dist = [[INF]*W for _ in range(H)]
    if maze[0][0]=='#' or maze[H-1][W-1]=='#':
        print(-1)
        sys.exit()
    else:
        dist[0][0] = 0

    que = deque([[0,0]])
    while que:
        y,x = que.popleft()
        for dy, dx in d:
            ny = y+dy
            nx = x+dx
            if 0<=ny<H and 0<=nx<W and maze[ny][nx]=='.' and dist[y][x]+1<dist[ny][nx]:
                dist[ny][nx] = dist[y][x]+1
                que.append([ny,nx])
    if dist[H-1][W-1] == INF:
        print(-1)
    else:
        count = 0
        for c in maze:
            count += c.count('.')
        print(count - dist[H-1][W-1] -1)




if __name__ == '__main__':
    main()

