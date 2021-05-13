import sys

H, W = map(int, sys.stdin.readline().split())
h, w = map(int, sys.stdin.readline().split())

print(H * W - W * h - H * w + h * w)