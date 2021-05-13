W, H, x, y = map(int, input().split())

First = min(W * (H - y), W * y)
Second = min(x * H, (W - x) * H)
check = 0
if x * 2 == W and y * 2 == H:
    check = 1
print(W * H / 2, check)
