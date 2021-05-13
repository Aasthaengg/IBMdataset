H, W = map(int, input().split())
h, w = map(int, input().split())

total = H * W
black = h * W + w * (H - h)
ans = total - black

print(ans)