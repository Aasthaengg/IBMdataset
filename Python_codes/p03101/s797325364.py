H, W = map(int, input().split())
h, w = map(int, input().split())

hyo = H * W
hr = h * W
wr = w * (H-h)

ans = (hyo - (hr+wr))
print(ans)