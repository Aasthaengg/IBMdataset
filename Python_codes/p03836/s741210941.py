sx, sy, tx, ty = map(int, input().split())
X, Y = tx - sx, ty - sy
for d, n in zip("RULD", [X, Y, X, Y]):
    print(d * n, end="")
for d, n in zip("DRULULDR", [1, X + 1, Y + 1, 1, 1, X + 1, Y + 1, 1]):
    print(d * n, end="")
print()