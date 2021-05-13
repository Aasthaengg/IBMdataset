import sys
H, W = map(int, sys.stdin.readline().rstrip().split())
h, w = map(int, sys.stdin.readline().rstrip().split())
print((H - h) * (W - w))