h, w, a, b = map(int, input().split())
d = [[0]*w for _ in range(h)]
for i in range(b):
    for j in range(a, w):
        d[i][j] = 1
for i in range(a):
    for j in range(b, h):
        d[j][i] = 1
for i in d: print(*i, sep="")