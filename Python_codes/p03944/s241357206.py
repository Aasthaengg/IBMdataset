w, h, n = map(int, input().split())

xy = []
for i in range(h):
    tmp = [0] * w
    xy.append(tmp)


lis = []
for _ in range(n):
    t = list(map(int, input().split()))
    lis.append(t)

for i in lis:
    if i[2] == 1:
        for j in range(h):
            for k in range(i[0]):
                xy[j][k] = 1
    elif i[2] == 2:
        for j in range(h):
            for k in range(i[0], w):
                xy[j][k] = 1
    elif i[2] == 3:
        for j in range(i[1]):
            for k in range(w):
                xy[j][k] = 1
    elif i[2] == 4:
        for j in range(i[1], h):
            for k in range(w):
                xy[j][k] = 1

ans = 0
for i in xy:
    for j in i:
        if j == 0:
            ans += 1

print(ans)