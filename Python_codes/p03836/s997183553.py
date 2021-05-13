
(sx, sy, tx, ty) = tuple(map(int, input().split()))

(dx, dy) = (tx - sx, ty - sy)

ans = "R" * dx + "U" * dy \
    + "L" * dx + "D" * dy \
    + "D" + "R" * (dx + 1) + "U" * (dy + 1) + "L" \
    + "U" + "L" * (dx + 1) + "D" * (dy + 1) + "R"

print(ans)
