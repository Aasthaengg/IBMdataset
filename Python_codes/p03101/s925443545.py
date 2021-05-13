H, W = map(int, input().split())
h, w = map(int, input().split())

HW = H * W
hW = h * W
Hw = H * w - h * w
print(HW - hW - Hw)