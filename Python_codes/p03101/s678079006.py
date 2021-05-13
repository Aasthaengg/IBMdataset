H, W = map(int, input().split())
h, w = map(int, input().split())
cell = H * W
line = h * W
row = w * H - h * w
print(cell - line - row)