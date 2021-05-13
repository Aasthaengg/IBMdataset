w, h, n = map(int, input().split())
OPS = list(list(map(int, input().split())) for _ in range(n))
l, r, t, b = 0, w, h, 0
for i in OPS:
    if i[2] == 1 and i[0] > l:
        l = i[0]
    elif i[2] == 2 and i[0] < r:
        r = i[0]
    elif i[2] == 3 and i[1] > b:
        b = i[1]
    elif i[2] == 4 and i[1] < t:
        t = i[1]
print(max(r - l, 0) * max(t - b, 0))