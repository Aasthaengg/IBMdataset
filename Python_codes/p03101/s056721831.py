H, W = map(int, input().split())
h, w = map(int, input().split())
a = H * W
b = h * w
c = h * W
d = H * w
e = c + d - b
f = a - e
print(f)