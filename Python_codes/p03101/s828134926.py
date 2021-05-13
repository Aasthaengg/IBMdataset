from sys import stdin
H, W = [int(x) for x in stdin.readline().rstrip().split()]
h, w = [int(x) for x in stdin.readline().rstrip().split()]
print((H * W) - (h * W) - (w * H) + (h * w))