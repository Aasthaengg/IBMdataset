h, w, a, b = map(int, input().split())
l = [[0 for j in range(w)] for i in range(h)]
for i in range(b):
    for j in range(a):
        l[i][j] = 1
for i in range(b, h):
    for j in range(a, w):
        l[i][j] = 1
for i in l:
    print(*i, sep="")