h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

color = 0
cnt = 0
res = [[0] * w for _ in range(h)]
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            res[i][j] = color + 1
            cnt += 1
            if cnt == a[color]:
                color += 1
                cnt = 0
    else:
        for j in range(w-1, -1, -1):
            res[i][j] = color + 1
            cnt += 1
            if cnt == a[color]:
                color += 1
                cnt = 0

for i in range(h):
    for j in range(w):
        print(res[i][j], end=' ')
    print()