h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

color = [[0 for _ in range(w)] for _ in range(h)]
c = 0
for i in range(h*w):
    x = i // w
    y = i % w
    if x % 2:
        y = w - 1 - y
    if a[c] == 0:
        c += 1
    color[x][y] = c+1
    a[c] -= 1
for i in range(h):
    print(*color[i])