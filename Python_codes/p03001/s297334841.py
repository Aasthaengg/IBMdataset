W, H, x, y = map(int, input().split())
area = W * H / 2
multi = x * 2 == W and y * 2 == H
print(area, 1 if multi else 0)