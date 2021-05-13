W, H, x, y = map(int, input().split())
S = W*H/2
can = 1 if 2*x == W and 2*y == H else 0

print(S, can)