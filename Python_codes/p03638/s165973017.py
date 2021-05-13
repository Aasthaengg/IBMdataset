h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

color = []
for i in range(n):
    for j in range(a[i]):
        color.append(i + 1)

ans = [[0 for i in range(w)] for j in range(h)]

cnt = 0
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            ans[i][j] = color[cnt]
            cnt += 1
    else:
        for j in range(w):
            ans[i][w-1-j] = color[cnt]
            cnt += 1

for i in range(h):
    for j in range(w):
        if j == w - 1:
            print(ans[i][j])
        else:
            print(ans[i][j], end=" ")
