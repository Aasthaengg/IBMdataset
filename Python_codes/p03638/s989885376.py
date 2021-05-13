h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
color = []
for i, v in enumerate(a):
    for _ in range(v):
        color.append(i+1)
ans = [[0] * w for _ in range(h)]
q = 1
x, y = 0, -1
for i in range(h*w):
    if q == 1:
        if y == w-1:
            x += 1
            q = 0
        else:
            y += 1

    elif q == 0:
        if y == 0:
            x += 1
            q = 1
        else:
            y -= 1
    ans[x][y] = color[i]
for w in ans:
    print(*w)