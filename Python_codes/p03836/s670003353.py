# ABC 051: C – Back and Forth
sx, sy, tx, ty = [int(i) for i in input().split()]

dx = tx - sx
dy = ty - sy

# r1
r1 = 'U' * dy + 'R' * dx

# r2
r2 = 'D' * dy + 'L' * dx

# r3
r3 = 'L' + 'U' * (dy + 1) + 'R' * (dx + 1) + 'D'

# r4
r4 = 'R' + 'D' * (dy + 1) + 'L' * (dx + 1) + 'U'

print(r1 + r2 + r3 + r4)