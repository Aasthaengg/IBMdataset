sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

res = ""

res = "R" * dx + "U" * dy + "L" * dx + "D" * (dy + 1) \
      + "R" * (dx + 1) + "U" * (dy + 1) + "L" + "U" \
      + "L" * (dx + 1) + "D" * (dy + 1) + "R"

print(res)
