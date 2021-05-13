w0, h0 = 0, 0
w, h, n = map(int, input().split())
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and w0 < x:
        w0 = x
    elif a == 2 and x < w:
        w = x
    elif a == 3 and h0 < y:
        h0 = y
    elif a == 4 and y < h:
        h = y

print([0, (w - w0) * (h - h0)][w - w0 > 0 < h - h0])