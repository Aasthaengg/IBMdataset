W, H, x, y = map(int, input().split())

area = W * H / 2
ways = 0
if x == W / 2 and y == H / 2:
    ways += 1

print(area, ways)
