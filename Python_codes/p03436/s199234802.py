import sys
from collections import deque

input = sys.stdin.readline
digtmp = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    H, W = map(int, input().split())
    grid = []; cnt = 0
    grid.append(['#'] * (W+2))
    for _ in range(H):
        tmp = list(input())
        cnt += sum([1 for x in tmp if x == '#'])
        grid.append(['#'] + tmp + ['#'])
    grid.append(['#'] * (W+2))

    que = deque([(1, 1)])
    grid[1][1] = 1
    for _ in range(10000):
        a, b = que.popleft()
        for dx, dy in digtmp:
            x, y = (a + dx, b + dy)
            if grid[x][y] == '.':
                grid[x][y] = grid[a][b] + 1
                que.append((x, y))
        if len(que) == 0:
            break
    if grid[H][W] in ['#', '.']:
        print(-1)
        return
    ans = H*W - grid[H][W] - cnt
    print(ans)

if __name__ == "__main__":
    main()
