import sys

W, H, x, y = map(int, sys.stdin.readline().split())

print(W*H / 2, 1 if 2 * x == W and 2 * y == H else 0)