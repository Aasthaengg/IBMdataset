from collections import deque

h, w = map(int, input().split())

d = deque()
op = [[-1] * w for i in range(h)]

for i in range(h):
    s = input().rstrip()
    for j in range(len(s)):
        if s[j] == '#':
            d.append((i, j, 0))
            op[i][j] = 0

while d:
    i, j, step = d.popleft()

    for i2, j2 in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= i2 < h and 0 <= j2 < w:
            if op[i2][j2] == -1:
                d.append((i2, j2, step+1))
                op[i2][j2] = step + 1

print(max([max(op[i]) for i in range(h)]))
