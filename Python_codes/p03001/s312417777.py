import sys

W, H, x, y = map(int, sys.stdin.readline().split())

if 2*x == W and 2*y == H:
    multi = 1
else:
    multi = 0

print(W*H/2, multi)