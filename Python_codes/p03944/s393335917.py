W, H, n = map(int, input().split())
w, h = 0, 0

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and w < x: w = x
    elif a == 2 and W > x: W = x
    elif a == 3 and h < y: h = y
    elif a == 4 and H > y: H = y

print(max(W - w, 0) * max(H - h, 0))
