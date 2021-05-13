H, W = map(int,input().split())

h, w = map(int,input().split())

S = H * W

left = S - ((h * W) + (w * H) - (w * h))

print(left)
