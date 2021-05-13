w, h, n = list(map(int, input().split()))
c = [[] for _ in range(n)]
g = [[0] * w for _ in range(h)]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for H in range(h):
            for W in range(x):
                g[H][W] = 1
    elif a == 2:
        for H in range(h):
            for W in range(x, w):
                g[H][W] = 1
    elif a == 3:
        for H in range(y):
            for W in range(w):
                g[H][W] = 1
    else:
        for H in range(y, h):
            for W in range(w):
                g[H][W] = 1
cnt = 0
for i in g:
    cnt += i.count(0)
print(cnt)
