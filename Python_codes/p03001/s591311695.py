W, H, x, y = list(map(int, input().split()))
s_max = W * H / 2
m = 1 if (x == W / 2) and (y == H / 2) else 0
print(s_max, m)
