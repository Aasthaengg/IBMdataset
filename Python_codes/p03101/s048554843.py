H, W = map(int, input().split())
h, w = map(int, input().split())

a = H * W
b = h * W
c = w * (H - h)
d = a - (b + c)

print(d)