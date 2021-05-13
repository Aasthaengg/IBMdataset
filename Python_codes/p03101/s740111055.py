H, W = map(int, input().split())
h, w = map(int, input().split())
s = H * W
s1 = h * W
s2 = H * w
s3 = s1 + s2 - h * w
print(s - s3)
