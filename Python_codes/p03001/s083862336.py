W, H, x, y = [int(_) for _ in input().split()]

ans1 = W / 2 * H
if x == W / 2 and y == H / 2:
    ans2 = 1
else:
    ans2 = 0

print(f"{ans1} {ans2}")
