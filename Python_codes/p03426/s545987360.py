h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [0 for _ in range(h * w)]
for i in range(h):
    for j in range(w):
        b[a[i][j] - 1] = [i, j]
c = [0 for _ in range(h * w)]
m = 0
l = 0
i, j = 0, 0
for _ in range(h * w):
    c[i] = abs(b[i][0] - b[j][0]) + abs(b[i][1] - b[j][1])
    j = i
    if i >= d:
        c[i] += c[i - d]
    i += d
    if i >= h * w:
        l += 1
        i = l
        j = l
c.insert(0, 0)
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(c[r] - c[l])