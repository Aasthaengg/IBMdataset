w, h, n = map(int, input().split(" "))
area = [[0] * w for i in range(h)]

for i in range(n):
    x, y , a = map(int, input().split(" "))
    if a == 1:
        for j in range(x):
            for k in range(h):
                area[k][j] = 1
    elif a == 2:
        for j in range(x, w):
            for k in range(h):
                area[k][j] = 1
    elif a == 3:
        for j in range(w):
            for k in range(y):
                area[k][j] = 1
    elif a == 4:
        for j in range(w):
            for k in range(y, h):
                area[k][j] = 1
c = 0
for i in range(h):
    for j in range(w):
        if area[i][j] == 0:
            c += 1
print(c)