sx, sy, tx, ty = [int(s) for s in input().split(" ")]
diff = [tx - sx, ty - sy]

print("R" * diff[0] + "U" * diff[1] + "L" * diff[0] + "D" * diff[1] + "D" + "R" * (diff[0] + 1) + "U" * (diff[1] + 1) + "L" + "U" + "L" * (diff[0] + 1) + "D" * (diff[1] + 1) + "R")