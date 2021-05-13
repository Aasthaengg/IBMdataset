from collections import deque
import sys
input = sys.stdin.readline
q = deque()
h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
x = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            for k in x:
                if 0 <= i + k[0] < h and 0 <= j + k[1] < w and a[i + k[0]][j + k[1]] == ".":
                    a[i + k[0]][j + k[1]] = "0"
                    q.append([i + k[0], j + k[1], 1])
ans = 0
while q:
    u, v, res = q.popleft()
    for k in x:
        if 0 <= u + k[0] < h and 0 <= v + k[1] < w and a[u + k[0]][v + k[1]] == ".":
            a[u + k[0]][v + k[1]] = "0"
            q.append((u + k[0], v + k[1], res + 1))
            ans = res + 1
print(ans)