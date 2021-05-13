import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
field = []
q = deque()
for i in range(H):
    line = []
    A = input()
    for j in range(W):
        if A[j] == ".":
            line.append(True)
        else:
            line.append(False)
            q.append(((j, i), 0))
    field.append(line)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

ans = 0

while len(q) != 0:
    (x, y), d = q.popleft()
    ans = max(d, ans)
    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if 0 <= nx <= W - 1 and 0 <= ny <= H - 1 and field[ny][nx]:
            field[ny][nx] = False
            q.append(((nx, ny), d+1))

print(ans)
