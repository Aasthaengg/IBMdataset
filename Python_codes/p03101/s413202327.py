H, W = map(int, input().split())
h, w = map(int, input().split())

area = H * W
white = area - h * W - (H-h) * w
print(white)