sx, sy, tx, ty = map(int, input().split())
X, Y = tx - sx, ty - sy
for d, n in zip("RULDRULULDR", [X, Y, X, Y + 1, X + 1, Y + 1, 1, 1, X + 1, Y + 1, 1]):
    print(d * n, end="")
print()