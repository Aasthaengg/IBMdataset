h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))

ans = [[0]*w for i in range(h)]

now = 0
for color, count in enumerate(A, 1):
    for idx in range(now, now+count):
        y = idx // w
        x = idx % w
        if y % 2 == 1:
            x = -x-1
        ans[y][x] = color

    now += count

for line in ans:
    print(*line)