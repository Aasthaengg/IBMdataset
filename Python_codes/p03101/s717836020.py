H, W = list(map(int, input().split()))
h, w = list(map(int, input().split()))
t, hw, ans = 0, 0, 0
hw = h * w
t = H * W
print(t + hw - h * W - w * H)