def resolve():
    sx, sy, tx, ty = [int(i) for i in input().split()]
    x = tx - sx
    y = ty - sy
    print("U" * y, "R" * x, sep="", end="")
    print("D" * y, "L" * x, sep="", end="")
    print("L", "U" * y, "U", "R" * x, "RD", sep="", end="")
    print("R", "D" * y, "DL", "L" * x, "U", sep="", end="")
    print()

resolve()

