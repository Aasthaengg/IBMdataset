# input
H, W = map(int, input().split())
h, w = map(int, input().split())

# check
if (H, W) == (h, w):
    print(0)
else:
    print(H * W - ((W * h) + (H * w) - (h * w)))