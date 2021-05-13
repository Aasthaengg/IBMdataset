sx, sy, tx, ty = map(int, input().split())
vertical = ty - sy
side =  tx - sx
cycle1 = "U" * vertical + "R" * side + "D" * vertical + "L" * side
cycle2 = "L" + "U" * (vertical + 1) + "R" * (side + 1) + "D" + "R" + "D" * (vertical + 1) + "L" * (side + 1) + "U"
print(cycle1 + cycle2) 