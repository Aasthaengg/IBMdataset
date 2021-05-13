import sys
import collections
from collections import deque

input = sys.stdin.readline
digtmp = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    H, W = map(int, input().split())
    field = []
    white = 0
    for h in range(H):
        tmp = list(input()[:-1])
        white += collections.Counter(tmp)['.']
        field.append(tmp)

    # BFS
    field[0][0] = 1
    que = deque([(0, 0)])
    while True:
        fr_x, fr_y = que.popleft()
        cnt = field[fr_x][fr_y]
        for d_x, d_y in digtmp:
            to_x = fr_x + d_x
            to_y = fr_y + d_y
            if 0 <= to_x < H and 0 <= to_y < W:
                if field[to_x][to_y] == '.':
                    field[to_x][to_y] = cnt + 1
                    que.append((to_x, to_y))
                else:
                    continue
        if len(que) == 0:
            break

    goal = field[H-1][W-1]
    if goal in ['.', '#']:
        print(-1)
        return
    ans = white - goal
    print(ans)
    return

if __name__ == "__main__":
    main()
