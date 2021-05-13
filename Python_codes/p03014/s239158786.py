h, w = map(int, input().split())
s = [input() for i in range(h)]

yoko = [[0] * w for i in range(h)]
for i in range(h):
    tmp = 0
    l = 0
    for j in range(w + 1):
        if j == w or s[i][j] == "#":
            for k in range(l, j):
                yoko[i][k] = tmp
            l = j + 1
            tmp = 0
        else:
            tmp += 1
            
tate = [[0] * w for i in range(h)]
for j in range(w):
    tmp = 0
    l = 0
    for i in range(h + 1):
        if i == h or s[i][j] == "#":
            for k in range(l, i):
                tate[k][j] = tmp
            l = i + 1
            tmp = 0
        else:
            tmp += 1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, tate[i][j] + yoko[i][j])
print(ans - 1)