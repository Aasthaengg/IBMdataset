H, W, h, w = map(int, open(0).read().split())

cnt = H * W
cnt -= h * W
cnt -= H * w
cnt += h * w

print(cnt)