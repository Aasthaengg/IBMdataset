# https://atcoder.jp/contests/agc033/tasks/agc033_a

from collections import deque
h, w = map(int, input().split())

matrix = []
for _ in range(h):
    matrix.append(list(input()))

def bfs(matrix):
    # 上、右、下、左
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    q = deque()
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '#':
                q.append((i, j))
    ans = 0
    next_q = deque()
    while q:
        y, x = q.popleft()
        for i in range(4):
            next_y = dy[i] + y
            next_x = dx[i] + x
            if 0 <= next_y < h and 0 <= next_x < w and matrix[next_y][next_x] == '.':
                matrix[next_y][next_x] = '#'
                next_q.append((next_y, next_x))
        if not q and next_q:
            q = next_q
            next_q = deque()
            ans += 1
    return ans

ans = bfs(matrix)
print(ans)