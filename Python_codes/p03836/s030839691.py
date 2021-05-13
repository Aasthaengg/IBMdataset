sx, sy, tx, ty = [int(a) for a in input().split()]

dx = tx - sx
dy = ty - sy

txt = ""
# route 1
txt += dy*"U" + dx*"R"
# route 2
txt += dy*"D" + dx*"L"
# route 3
txt += "L" + (dy+1)*"U" + (dx+1)*"R" + "D"
# route 4
txt += "R" + (dy+1)*"D" + (dx+1)*"L" + "U"

print(txt)