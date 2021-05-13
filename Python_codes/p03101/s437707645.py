H, W = map(int, input().split())
h, w = map(int, input().split())

white_start = H * W
black = w * H + (W - w) * h
white_end = white_start - black
print(white_end)