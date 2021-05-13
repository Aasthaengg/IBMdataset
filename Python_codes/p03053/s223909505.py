import sys
from collections import deque

input = sys.stdin.readline
h, w = map(int, input().rstrip("\n").split())
matrix = [[-1 for j in range(w)] for i in range(h)]
queue = deque()
for i in range(h):
    cells = list(input().rstrip("\n"))
    for j, cell in enumerate(cells):
        if cell == "#":
            matrix[i][j] = 0
            queue.append((i, j))
while queue:
    i, j = queue.popleft()
    for i_diff, j_diff in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        i_current = i + i_diff
        j_current = j + j_diff
        if (
            0 <= i_current < h
            and 0 <= j_current < w
            and matrix[i_current][j_current] == -1
        ):
            matrix[i_current][j_current] = matrix[i][j] + 1
            queue.append((i_current, j_current))

max_step = max([max(row) for row in matrix])
print(max_step)