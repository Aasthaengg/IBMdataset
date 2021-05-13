W, H, x, y = map(int, input().split())
S = W * H
ans = float(S / 2.0)


gx, gy = W / 2.0, H / 2.0

if (gx == x) and (gy == y):
    tar = '1'
else:
    tar = '0'

print(ans, tar)
