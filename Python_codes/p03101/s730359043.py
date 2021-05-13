H, W = map(int, input().split())
h, w = map(int, input().split())

all = H * W

ans = all - (h * W) - (w * H) + w * h
print(ans)