from collections import deque

h, w = list(map(int, input().split()))

s = [list(input()) for _ in range(h)]

yo = [[0] * w for _ in range(h)]
q = deque([])
c = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            q.append((i, j))
            c += 1
        
        if s[i][j] == "#" or j == w-1:
            while len(q) > 0:
                x, y = q.pop()
                yo[x][y] = c
            c = 0



m = 0

c = 0
for j in range(w):
    for i in range(h):
        if s[i][j] == ".":
            q.append((i, j))
            c += 1

        if s[i][j] == "#" or i == h-1:
            while len(q) > 0:
                x, y = q.pop()
                m = max(m, yo[x][y] + c - 1)
            c = 0
print(m)
