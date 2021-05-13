W, H, x, y = map(int, input().split())
p = 0
if (x, y) == (W/2, H/2):
    p = 1
print('{} {}'.format(W*H/2, p))